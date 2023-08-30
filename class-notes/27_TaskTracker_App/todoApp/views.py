from django.shortcuts import render
from .models import Todo


#!### FBV ####
def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todos":todos,
    }
    return render(request, "todoApp/list.html", context)
#   return render(request, html, {{ "todos":todos }} )
#   return render(request, html, context )
