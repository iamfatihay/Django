from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def home(request):
    return HttpResponse('<h1>API Page</h1>')

#? ########################
#?     http methods
#? ########################
#* GET         veri cagir
#* POST        create
#* DELETE      veri sil
#* PUT         veri degistir
#* PATCH       parcali olarak veri degistir

@api_view(["GET"])
def student_api(request):
    students = Student.objects.all()  # veri tipi queryset
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)   # JSON formatinda

@api_view(["POST"])
def student_create(request):
    # print(request.data)
    # return Response("deneme")
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {"message":"Created successfully!"}
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def student_detail(request, pk):
    # student = Student.objects.get(id=pk)
    student = get_object_or_404(Student, pk=pk)
    message = {"message":"Successfull!"}
    return Response(message)   


@api_view(["DELETE"])
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    message = {"message":"Deleted successfully!"}
    return Response(message)   

# @api_view(["PUT"])
@api_view(["PATCH"])
def student_update(request, pk):

    student = get_object_or_404(Student, pk=pk)
    # PUT
    # serializer = StudentSerializer(instance=student, data=request.data)
    # PATCH
    serializer = StudentSerializer(instance=student, data=request.data, partial=True)
    if serializer.is_valid():  
        serializer.save()
        message = {"message":"Updated successfully!"}
        return Response(message)   
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)