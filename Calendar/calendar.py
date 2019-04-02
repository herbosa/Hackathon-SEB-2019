#!/usr/bin/env python3

from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
DAYS_SHORT_ID = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
NOW = datetime.datetime.utcnow()


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



class WorkingDay:
    def __init__(self, day: int, month: int, year: int,
                       start: int = 540, end: int = 1440):
        self.day = day
        self.month = month
        self.year = year
        self.events: [(int, Task)] = [(start, None), (end, None)]

    def add_event(self, event: (int, Task)) -> bool:
        size = len(self.events) - 1

        for i in range(size):
            if (event[0] == self.events[i][0] and self.events[i][1] == None):
                self.events[i] = event
                return True
            elif (event[0] > self.events[i][0] and event[0] < self.events[i + 1][0]):
                self.events.insert(i + 1, event)
                return True
        return False

    def check_duration_availability(self, duration: int) -> int:
        size = len(self.events) - 1

        for i in range(size):
            if (self.events[i + 1][0] - self.events[i][0] > duration):
                return self.events[0][0] + (i * 60)
        return 0

    def __repr__(self):
        """ Create string representation of WorkingDay class """
        string = ""
        for event in self.events:
            string = string + "%d %s\n" % (event[0], event[1])
        return (string)


class Employee:
    def __init__(self, email: str, skills: [str]):
        self.email = email
        self.skills = skills
        self.days = []
        for i in range(len(DAYS_SHORT_ID)):
            self.days.append(WorkingDay(NOW.day + i, NOW.month, NOW.year))

    def fill_day(self, events: [datetime]):
        for time in events:
            for weekDay in self.days:
                if (time.day != weekDay.day or time.month != weekDay.month
                        or time.year != weekDay.year):
                    continue
                if weekDay.add_event((time.hour * 60, None)) == True:
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

    def find_availability_for_task(self, task) -> bool:
        priority = []
        time = 0

        if not self._check_skills(task.description.skills):
            return False
        priority = self._create_priority(task.preferences)
        for pos in priority:
            if pos < len(self.days):
                time = self.days[pos].check_duration_availability(task.description.time)
                if time:
                    return self.days[pos].add_event((time, task))
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
        start = event['start'].get('dateTime', event['start'].get('date'))
        date_events.append(datetime.datetime.strptime(start[:-6], '%Y-%m-%dT%H:%M:%S'))
    return (date_events)


def main(): 
    filename = "tasks.json"
    with open(filename, 'r') as f: 
        data = json.load(f)
    service = init_mail_service()

    events = get_event(service, NOW.isoformat() + 'Z') 
    print(events)
    company = Company("test", [Employee("test.test@test.com", ["Swift", "C"])])
    company.employees[0].fill_day(events)
    for elem in data["tasks"]:
        company.employees[0].find_availability_for_task(Task(elem))

    for elem in company.employees[0].days:
        print(elem)
  
if __name__ == '__main__':
    main()
