# from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("model 2 dersine hosgeldiniz")
