from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from django.shortcuts import get_object_or_404

from .models import Todo
from .serializers import TodoSerializer

from django.http import HttpResponse

def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to Todo APP</h1></center>'
    )

@api_view(["GET", "POST"])
def todo_list_create(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def todo_get_delete_update(request, pk):
    todo = get_object_or_404(Todo, id=pk)

    if request.method == "GET":       
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = TodoSerializer(data=serializer.data, instance=todo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        todo.delete()
        message={"message":"Successfully deleted!"}
        return Response(message, status=HTTP_400_BAD_REQUEST)