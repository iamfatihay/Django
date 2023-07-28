from django.urls import path
from .views import home, todo_list_create

urlpatterns = [
    path("", home),
    path("list", todo_list_create),
]
