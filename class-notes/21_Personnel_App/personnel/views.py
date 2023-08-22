from django.shortcuts import render
from .serializers import DepartmentSerializer, PersonnelSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Department, Personnel
from rest_framework.permissions import IsAdminUser
from .permissions import IsStaffOrReadOnly

# Create your views here.
class DepartmentView(ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsStaffOrReadOnly]


class PersonnelView(ListCreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    permission_classes = [IsAdminUser]

class Personnel_GPD_UPDATE_View(RetrieveUpdateDestroyAPIView):   #! GPD = Get, post, destroy
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    # permission_classes = [IsAdminUser]