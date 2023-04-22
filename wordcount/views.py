from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'text': 'work on it!!!'})


def eggs(request):
    return HttpResponse('i like eggs')
