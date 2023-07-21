from django.urls import path
from .views import home, students, teacher

urlpatterns = [
    path('', home),
    path('students/', students),
    path('teacher/', teacher),
]
