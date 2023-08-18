from django.shortcuts import render
from .serializers import DepartmentSerializer, PersonnelSerializer
from rest_framework.generics import ListCreateAPIView
from .models import Department, Personnel
from rest_framework.permissions import IsAdminUser

# Create your views here.
class DepartmentView(ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAdminUser,]


class PersonnelView(ListCreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()