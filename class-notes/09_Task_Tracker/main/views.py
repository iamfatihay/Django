from django.http import HttpResponse

def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to Task Tracker</h1></center>'
    )