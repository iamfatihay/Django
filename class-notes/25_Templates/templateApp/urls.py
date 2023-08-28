from django.urls import path,include
from .views import home,body
urlpatterns = [
    path('', home),
    path('tmp', body)
]
