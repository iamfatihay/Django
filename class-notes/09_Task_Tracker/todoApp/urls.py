from django.urls import path, include
from .views import home, todo_list_create, todo_get_delete_update, Todos, TodosRUD, TodosMVS
from rest_framework import routers

router=routers.DefaultRouter()
router.register("todo", TodosMVS)


urlpatterns = [
    path("", home),
    #* FBV (function based view)
    # path("list", todo_list_create),
    # path("list/<int:pk>", todo_get_delete_update),
    #* CBV (Class based view)
    # path("todo", Todos.as_view()),
    # path("todorud/<int:pk>", TodosRUD.as_view()),
    #* MVS 
    path("", include(router.urls)),
]
