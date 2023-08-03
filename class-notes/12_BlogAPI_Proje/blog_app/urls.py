from django.urls import path, include
from .views import Blog, home, Category
from rest_framework import routers

router=routers.DefaultRouter()
router.register("blog", Blog)
router.register('categories', Category)

urlpatterns = router.urls


# urlpatterns = [
#     path("", home),
#     #* FBV (function based view)
#     # path("list", todo_list_create),
#     # path("list/<int:pk>", todo_get_delete_update),
#     #* CBV (Class based view)
#     # path("todo", Todos.as_view()),
#     # path("todorud/<int:pk>", TodosRUD.as_view()),
#     #* MVS 
#     path("", include(router.urls)),
# ]
