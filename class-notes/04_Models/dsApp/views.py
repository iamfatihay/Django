from django.shortcuts import render
from django.http import HttpResponse


def dswelcome(request):
    return HttpResponse("DS sayfasina hosgeldiiz!")
