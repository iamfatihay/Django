from django.urls import path, include
from .views import todo_list, todo_add, todo_update, todo_delete, TodoListView, TodoCreateView, TodoUpdateView,TodoDeleteView
urlpatterns = [
    ## FBV ##
    #path("",todo_list, name="todo_list"),
    #path("add",todo_add, name="todo_add"),
    #path("update/<int:pk>",todo_update, name="todo_update"),
    #path("delete/<int:pk>",todo_delete, name="todo_delete"),

    ## CBV ##
    #path("",TodoListView.as_view(), name="todo_list"),
    #path("add",TodoCreateView.as_view(), name="todo_add"),
    #path("update/<int:pk>",TodoUpdateView.as_view(), name="todo_update"),
    #path("delete/<int:pk>",TodoDeleteView.as_view(), name="todo_delete"),
]