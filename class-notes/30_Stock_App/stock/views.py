from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,DjangoModelPermissions

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import(
    Category,
    Brand,
    Product,
    Firm,
    Purchases,
    Sales,
    
)
from .serializers import(
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
    # Firm,
    # Purchases,
    # Sales,
    
)
# Create your views here.

class CategoryView(ModelViewSet):
    
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    # permission_classes=[DjangoModelPermissions]
    ## filter ve search 
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['name']
    search_fields=['name']


class BrandView(ModelViewSet):
    
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer
    # permission_classes=[DjangoModelPermissions]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['name']
    search_fields=['name']


class ProductView(ModelViewSet):
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # permission_classes=[DjangoModelPermissions]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['name']
    search_fields=['name']