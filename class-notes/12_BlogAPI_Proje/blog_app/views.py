from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from .serializers import BlogSerializer, CategorySerializer
from .models import Blog, Category

def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to Todo APP</h1></center>'
    )

class Blog(ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class Category(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer