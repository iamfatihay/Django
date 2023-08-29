from django.urls import path,include
from .views import home,body,studentView, student_addView
urlpatterns = [
    path('', body),
    path('home', home),
    path('student', studentView),
    # forms
    path('add', student_addView)
]
