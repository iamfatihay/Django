from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world!")

def students(request):
    return HttpResponse("Hi students!")

def teacher(request):
    return HttpResponse("Hi teacher!")

