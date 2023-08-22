from django.shortcuts import render
from .serializers import DepartmentSerializer, PersonnelSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Department, Personnel
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsStaffOrReadOnly
from rest_framework.response import Response
from rest_framework import status

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
    permission_classes = [IsAuthenticatedOrReadOnly]  #! eger authentice kullanici ise get put delete yapabilir, degilse sadece get

    #* Burada put ve delete islemlerini override yaptik
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user.is_staff and (instance.create_user == self.request.user):
            return self.update(request, *args, **kwargs)
        else:
            data = {
                "message": "You are not authorized to perform this operation"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.destroy(request, *args, **kwargs)
        else:
            data = {
                "message": "You are not authorized to perform this operation"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)