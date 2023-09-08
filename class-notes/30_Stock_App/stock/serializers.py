from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Category,Brand,Firm,Purchases,Sales,Product


class CategorySerializer(ModelSerializer):
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = (
            'id','name','product_count'
        )
    
    def get_product_count(self,obj):
        return obj.products.count()
        # return Product.objects.filter(category_id=obj_id).count()

class FirmSerializer(ModelSerializer):
    class Meta:
        model = Firm
        fields = ("__all__")


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ("__all__")


class ProductSerializer(ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = (
            'category',
            'category_id',
            'brand',
            'brand_id',
            'name',
            'stock',
        )


class CategoryProductSerializer(ModelSerializer):
    product_count = serializers.SerializerMethodField()
    products = ProductSerializer(many=True)
    #! buraya modeldeki related_name ile isimler uyusmasi gerekiyor
    class Meta:
        model = Category
        fields = (
            'id','name','product_count', 'products'
        )
    
    def get_product_count(self,obj):
        return obj.products.count()
        # return Product.objects.filter(category_id=obj_id).count()


class PurchasesSerializer(ModelSerializer):
    user=serializers.SlugRelatedField
    firm=serializers.StringRelatedField()
    firm_id=serializers.IntegerField()
    brand=serializers.StringRelatedField()
    brand_id=serializers.IntegerField()
    product=serializers.StringRelatedField()
    product_id=serializers.IntegerField()
    class Meta:
        model=Purchases
        fields=(
            "user",
            "firm",
            "firm_id",
            "brand",
            "brand_id",
            "product",
            "product_id",
            "quantity",
            "price",
            "price_total",
            )
        read_only_fields = ('price_total',)
    
    # def get_product_count(self,obj):
    #     return obj.products.count()
        # return Product.objects.filter(category_id=obj_id).count()

