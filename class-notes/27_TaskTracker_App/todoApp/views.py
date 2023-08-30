from django.shortcuts import render
from .models import Todo


#!### FBV ####
def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos,
    }
    return render(request, "todoApp/list.html", context)


#   return render(request, html, {{ "todos":todos }} )
#   return render(request, html, context )


from .forms import TodoForm
from django.shortcuts import redirect


def todo_add(request):
    form = TodoForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        form.save()
        return redirect("todo_list")
    return render(request, "todoApp/add.html", context)


def todo_update(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance = todo)
    

    if request.methof == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    context = {
        "form": form,
        "todo":todo
    }
    return render(request, "todoApp/update.html", context)
