from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1> Welcome to Django templates </h1>")


def body(request):
    context = {
        "name": "yunus"
    }
    return render(request, )