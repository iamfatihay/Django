from django.shortcuts import render
from .models import Todo

#!############
#!### FBV ####
#!############
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
    

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    context = {
        "form": form,
        # "todo":todo
    }
    return render(request, "todoApp/update.html", context)


def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("todo_list")

#!############
#!### CBV ####
#!############
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class TodoListView(ListView):
    model = Todo
    # eger farkli bir template kullanacaksaniz:
    # template_name = "todoApp/list.html"
    # template de default object_list olarak kullanilacak

from django.urls import reverse_lazy
class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")