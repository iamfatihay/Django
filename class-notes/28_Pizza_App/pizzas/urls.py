from django.urls import path, include
from .views import home, pizzas, order, my_orders, update, delete

urlpatterns = [
    path('', home, name="home"),
    path('pizzas', pizzas, name="pizzas"),
    path('order/<int:pk>', order, name="order"),
    path('my_orders/', my_orders, name="myorders"),
    path('update/<int:pk>', update, name="update"),
    path('delete/<int:pk>', delete, name="delete"),
]