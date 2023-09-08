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
    CategoryProductSerializer,
    BrandSerializer,
    ProductSerializer,
    FirmSerializer,
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
    # hangi serializer kullanilacagini sec
    
    def get_serializer_class(self):
        if self.request.query_params.get('name'):
            # parametre verirseniz istenen category e ait ürünleri verir
            return CategoryProductSerializer
        # Parametre vermezseniz category ler gelir
        return super().get_serializer_class()



# class CategoryProductView(ModelViewSet):
    
#     queryset=Category.objects.all()
#     serializer_class=CategoryProductSerializer
#     # permission_classes=[DjangoModelPermissions]
#     ## filter ve search 
#     filter_backends=[DjangoFilterBackend,filters.SearchFilter]
#     filterset_fields=['name']
#     search_fields=['name']


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


class FirmView(ModelViewSet):
    
    queryset=Firm.objects.all()
    serializer_class=FirmSerializer
    # permission_classes=[DjangoModelPermissions]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['name']
    search_fields=['name']