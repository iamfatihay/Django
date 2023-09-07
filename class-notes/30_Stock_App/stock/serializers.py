from rest_framework.serializers import ModelSerializer
from .models import Category,Brand,Firm,Purchases,Sales,Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ("__all__")


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ("__all__")