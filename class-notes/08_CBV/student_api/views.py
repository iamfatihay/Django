from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.


def home(request):
    return HttpResponse("<h1>API Page</h1>")


# ? ########################
# ?     http methods
# ? ########################
# * GET         veri cagir
# * POST        create
# * DELETE      veri sil
# * PUT         veri degistir
# * PATCH       parcali olarak veri degistir


@api_view(["GET"])
def student_api(request):
    students = Student.objects.all()  # veri tipi queryset
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)  # JSON formatinda


@api_view(["POST"])
def student_create(request):
    # print(request.data)
    # return Response("deneme")
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {"message": "Created successfully!"}
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def student_detail(request, pk):
    # student=Student.objects.get(id=pk)
    student = get_object_or_404(Student, pk=pk)
    serializer = StudentSerializer(student)
    message = {"Successfull"}
    data = {}
    data["message"] = message
    data["data"] = serializer.data
    return Response(data)


@api_view(["DELETE"])
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    message = {"message": "Deleted successfully!"}
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
        message = {"message": "Updated successfully!"}
        return Response(message)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ? ########################
# ?    CLASS BASED VIEWS
# ? ########################
# * ############  APIView Class ####################


class StudentListCreate(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {"message": "Created successfully!"}
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    def get_obj(self, pk):
        return get_object_or_404(Student, pk=pk)

    def get(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(data=request.data, instance=student)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(
            data=request.data, instance=student, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_obj(pk)
        student.delete()
        data = {"message": "Student succesfully deleted."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# * ############  Generic APIView and Mixins ####################
# GenericAPIView
""" One of the key benefits of class-based views is the way they allow you to compose bits of reusable behavior.
 REST framework takes advantage of this by providing a number of pre-built views that provide for commonly used patterns.

GenericAPIView class extends REST framework's APIView class, adding commonly required behavior for standard list 
and detail views. Some Basic Attributes and Methods. """


# mixins
""" The mixin classes provide the actions that are used to provide the basic view behavior.
 Note that the mixin classes provide action methods rather than defining the handler methods, such as .get() and .post(), directly.
This allows for more flexible composition of behavior. Tek başlarına bir işlem yapamazlar. GenericAPIView ile anlamlı oluyor """


class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # lookup_field = "last_name"   #! default u "pk" , istersek bu sekilde degistirebiliriz.

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

# * ############  Concrete View Classes ####################

class StudentCV(ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailCV(RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer