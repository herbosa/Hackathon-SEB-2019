#!/usr/bin/env python3

from __future__ import print_function
from datetime import datetime, date
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json


SCOPES = ['https://www.googleapis.com/auth/calendar']
DAYS_SHORT_ID = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
NOW = datetime.utcnow()


class Task(object):
    def __init__(self, data: dict):
        self.description = self.Description(data["description"])
        self.preferences = self.Preferences(data["preferences"])

    class Description:
        def __init__(self, data: dict):
            self.name: str = data["name"]
            self.time: int = data["time"]
            self.skills: [str] = data["skills"]

        def __str__(self):
            return "%s %d %s" % (self.name, self.time, self.skills)

    class Preferences:
        def __init__(self, data: dict):
            self.days: [str] = data["days"]
            self.attendees: [str] = data["attendees"]

        def __str__(self):
            return "%s %s" % (self.days, self.attendees)

    def __repr__(self):
        return "%s %s" % (self.description, self.preferences) 


class Event:
    def __init__(self, start: int, time: datetime, task: Task, duration: int = 0):
        self.start = start
        self.time = time
        self.task = task
        self.duration = duration
        if task:
            self.duration = task.description.time

    def __str__(self):
        return "%s %s" % (self.start, self.task)

    def __repr__(self):
        return "%s %s" % (self.start, self.task)

class WorkingDay:
    def __init__(self, day: int, month: int, year: int,
                       start: int = 540, end: int = 1440):
        self.day = day
        self.month = month
        self.year = year
        self.date = datetime(year, month, day)
        self.start = start
        self.end = end
        self.events: [Event] = []

    def add_event(self, event: Event) -> bool:
        size = len(self.events) - 1
        time = self.start

        if size <= 0:
            self.events.append(event)
            self.events.append(Event(event.start + event.duration, event.time,
                None, event.duration))
        for i in range(size):
            if (event.start == time and self.events[i].task == None):
                self.events[i] = event
                return True
            elif (event.start > time and event.start < self.events[i + 1].start):
                self.events.insert(i + 1, event)
                self.events.insert(i + 2, Event(event.start + event.duration, event.time, 
                    None, event.duration))
                return True
            time = self.events[i].start
        return False

    def check_duration_availability(self, duration: int) -> int:
        size = len(self.events)
        time = self.start

        if size == 0 and time - self.end != 0:
            return (self.start)
        for i in range(size):
            if (abs(time - self.events[i].start) > duration):
                return time + (i * 60)
            time = self.events[i].start
        if (time - self.end > duration):
            return time
        return 0

    def __repr__(self):
        """ Create string representation of WorkingDay class """
        string = ""
        for event in self.events:
            string = string + "%s" %s (event)
        return (string)


class Employee:
    def __init__(self, email: str, skills: [str]):
        self.email = email
        self.skills = skills
        self.days: [WorkingDay] = []
        for i in range(len(DAYS_SHORT_ID)):
            self.days.append(WorkingDay(NOW.day + i, NOW.month, NOW.year))

    def fill_day(self, events: [Event]):
        for event in events:
            for weekDay in self.days:
                if (event.time.day != weekDay.day or event.time.month != weekDay.month
                        or event.time.year != weekDay.year):
                    continue
                if weekDay.add_event(event) == True:
                    break

    def _create_priority(self, preferences) -> [int]:
        priority = []
        for day in preferences.days:
            priority.append(DAYS_SHORT_ID.index(day))
        for i in range(len(DAYS_SHORT_ID)):
            if i not in priority:
                priority.append(i)
        return priority

    def _check_skills(self, skills: [str]) -> bool:
        for skill in self.skills:
            for elem in skills:
                if elem == skill:
                    return True
        return False

    def find_availability_for_task(self, task: Task) -> bool:
        priority = []
        time = 0

        if not self._check_skills(task.description.skills):
            return False
        priority = self._create_priority(task.preferences)
        for pos in priority:
            print("")
            if pos < len(self.days):
                time = self.days[pos].check_duration_availability(task.description.time)
                if time:
                    return self.days[pos].add_event(Event(time, self.days[pos].date, task))
        return False


class Company:
    def __init__(self, name: str, employees: [Employee]):
        self.name = name
        self.employees = employees

def init_mail_service():
    """ Init calendar with credentials """
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return (build('calendar', 'v3', credentials=creds))


def get_event(service, date: str):
    """ Fetch current event in Google's Calendar """
    date_events = []

    events_result = service.events().list(calendarId='primary',
            timeMin=date, maxResults=10, singleEvents=True,
            orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
        start_string = event['start'].get('dateTime', event['start'].get('date'))
        start_datetime = datetime.strptime(start_string[:-6], "%Y-%m-%dT%H:%M:%S")

        end_string = event['end'].get('dateTime', event['end'].get('date'))
        end_datetime = datetime.strptime(end_string[:-6], "%Y-%m-%dT%H:%M:%S")

        diff = end_datetime - start_datetime

        date_events.append(Event(start_datetime.hour * 60 + start_datetime.minute,
            start_datetime, None, diff.total_seconds() / 60))
    return (date_events)

def create_event(service, event: Event):
    print(datetime(event.time.year, event.time.month, event.time.day,
                    int(event.start / 60), event.start % 60, 0).isoformat())
    json_event = {
            'summary': event.task.description.name,
            'start': {
                'dateTime': datetime(event.time.year, event.time.month, event.time.day,
                    int(event.start / 60), event.start % 60, 0).isoformat() + "+02:00",
            },
            'end': {
                'dateTime': datetime(event.time.year, event.time.month, event.time.day,
                    int((event.start + event.duration) / 60),
                    (event.start + event.duration) % 60, 0).isoformat() + "+02:00",
            },
    }
    service.events().insert(calendarId='primary', body=json_event).execute()


def main(): 
    filename = "tasks.json"
    with open(filename, 'r') as f: 
        data = json.load(f)

    service = init_mail_service()

    events = get_event(service, NOW.isoformat() + 'Z') 
    company = Company("test", [Employee("test.test@test.com", ["Swift", "C"])])
    company.employees[0].fill_day(events)
    for elem in data["tasks"]:
        company.employees[0].find_availability_for_task(Task(elem))

    for day in company.employees[0].days:
        print(day.events)
        for tmp in day.events:
            if tmp.task:
                create_event(service, tmp)
  
if __name__ == '__main__':
    main()
