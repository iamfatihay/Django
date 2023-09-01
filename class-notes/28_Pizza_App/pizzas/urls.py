from django.urls import path, include
from .views import home, pizzas

urlpatterns = [
    path('', home, name="home"),
    path('pizzas', pizzas, name="pizzas"),
]