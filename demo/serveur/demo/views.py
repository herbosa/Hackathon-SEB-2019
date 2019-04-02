from django.shortcuts import render
from django.http import HttpResponse
import requests

def distribute_mails(request, content):
    if request.method == 'GET':
        print(content)
        return HttpResponse("{\"status\": 200 }", content_type='application/json')
    else:
        return HttpResponse("{\"status\": 400 }", content_type='application/json')
