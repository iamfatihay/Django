from django.urls import path, include
from .views import DepartmentView, PersonnelView, Personnel_GPD_UPDATE_View

urlpatterns = [
    path("department/", DepartmentView.as_view()),
    path("personnel/", PersonnelView.as_view()),
    path("personnel/<int:pk>", Personnel_GPD_UPDATE_View.as_view()),
]
