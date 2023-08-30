from django.urls import path, include
from .views import todo_list
urlpatterns = [
    path("",todo_list),
]