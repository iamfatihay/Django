from django.urls import path, include
from .views import todo_list, todo_add, todo_update
urlpatterns = [
    path("",todo_list, name="todo_list"),
    path("add",todo_add),
    path("update/<int:pk>",todo_update),
]