from django.urls import path, include
from .views import (
    home,
    body,
    studentView,
    student_addView,
    StudentAddView,
    StudentListView,
    StudentDetailView,
    StudentUpdateView
)

urlpatterns = [
    path("", body),
    path("home", home),
    path("student", studentView, name="student"),  # name ler unique olmali
    # forms
    # fbv
    # path('add', student_addView),
    # cbv
    path("add", StudentAddView.as_view(), name="add"),
    path("list", StudentListView.as_view(), name="list"),
    path("detail/<int:pk>", StudentDetailView.as_view(), name="detail"),
    path("update/<int:pk>", StudentUpdateView.as_view(), name="update"),
]
