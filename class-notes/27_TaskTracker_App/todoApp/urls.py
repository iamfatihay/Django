from django.urls import path, include
from .views import todo_list, todo_add
urlpatterns = [
    path("",todo_list, name="todo_list"),
    path("add",todo_add),
]