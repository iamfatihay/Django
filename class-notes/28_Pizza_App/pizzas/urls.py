from django.urls import path, include
from .views import home, pizzas, order

urlpatterns = [
    path('', home, name="home"),
    path('pizzas', pizzas, name="pizzas"),
    path('order/<int:pk>', order, name="order"),
]