from django.shortcuts import render
from django.http import HttpResponse

def fswelcome(request):
    return HttpResponse("FS sayfasina hosgeldiniz!")
