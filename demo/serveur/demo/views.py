from django.shortcuts import render
from django.http import HttpResponse
import requests

DATA_JSON = """{
    "tasks": [
        { "description":
            { "name": "Reunion Projet info",
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

def distribute_mails(request, content):
    if request.method == 'GET':
        print(DATA_JSON)
        return HttpResponse("{\"status\": 200 }", content_type='application/json')
    else:
        return HttpResponse("{\"status\": 400 }", content_type='application/json')
