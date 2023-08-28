from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>welcome to django template</h1>')


def body(request):
     context={
          'name':'yunus'
          }
     return render(request,'templateApp/index.html',context)
    # return render(request,'templateApp/index.html',{'name':'yunus'})