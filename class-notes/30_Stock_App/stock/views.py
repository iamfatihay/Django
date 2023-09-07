from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Category,Brand,Firm,Purchases,Sales,Product
from .serializers import (
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
)


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

