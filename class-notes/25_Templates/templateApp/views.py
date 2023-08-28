from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1>welcome to django template</h1>")


def body(request):
    context = {
        "title": "clarusway",
        "path": "FS",
        "list": [
            "yunus",
            "ozlem",
            "fatih",
            "esra",
            "huseyin",
            "nihal",
            "emirhan",
            "halit",
            "irfan",
        ],
        "dict": {"k1": "value1", "k2": "value2"},
        "number": 0,
        "desc": "this template from APP dir"
    }
    return render(request, "templateApp/index.html", context)


# return render(request,'templateApp/index.html',{'name':'yunus'})
