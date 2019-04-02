from django.shortcuts import render
from django.http import HttpResponse
import requests

DATA_JSON = """{
    "tasks": [
        { "description":
            { "name": "mailbox IOS/Android application",
              "time": 60,
              "skills": ["Java", "Swift"]
            },
          "preferences":
            { "days": ["Mon", "Tue"],
              "attendees": ["Antoine.H"]
            }
        }
    ]
}"""

"I would like to take an appointement during 1h about the IOS/Android mailbox application."

DATA_JSON_2 = """{
    "tasks": [
        { "description":
            { "name": "for the April financial meeting.",
              "time": 30,
              "skills": ["Comptat"]
            },
          "preferences":
            { "days": ["Mon", "Tue"],
              attendees": [Quentin.H"]
            }
        }
    ]
}"""

"I need someone half an hour for the April financial meeting."

FIRST = True

def distribute_mails(request, content):
    global FIRST

    if request.method == 'GET':
        print(content)
        if FIRST:
            FIRST = False
            # Send DATA_JSON
            print(DATA_JSON)
        else:
            print(DATA_JSON_2)
            # Send DATA_JSON_2
        return HttpResponse("{\"status\": 200 }", content_type='application/json')
    else:
        return HttpResponse("{\"status\": 400 }", content_type='application/json')
