from django.shortcuts import render
from django.http import HttpResponse
from django import template
import os


def index(request):
    print os.getcwd()
    f = open('templates/chatBot/index.html')
    t = template.Template(f.read())
    f.close()
    return HttpResponse(t.render(template.Context({'data123': 'This is the test.'})))
    return render(request, "/chatBot/index.html")
