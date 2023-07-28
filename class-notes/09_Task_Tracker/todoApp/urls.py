from django.urls import path
from .views import home, todo_list_create, todo_get_delete_update

urlpatterns = [
    path("", home),
    #* FBV (function based view)
    path("list", todo_list_create),
    path("list/<int:pk>", todo_get_delete_update),
]
