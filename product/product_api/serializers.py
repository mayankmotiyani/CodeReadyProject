from rest_framework import serializers
from product.models import (
    Product,
    ProductCategory,
    ProductSubCategory
)

class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    owner = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ['id','product_name','product_price','owner']
    
    def get_product_name(self,instance):
        self.product_name = instance.product_name + " by " + instance.owner.username
        return self.product_name


class ProductSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubCategory
        fields = ['id','subcategory']

    def to_representation(self,instance):
        data = super(ProductSubCategorySerializer,self).to_representation(instance)
        data[data['subcategory']] = ProductSerializer(Product.objects.filter(product_category_id=data['id']),many=True).data
        return data

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id','category']

    def to_representation(self,instance):
        data = super(ProductCategorySerializer,self).to_representation(instance)
        data[data['category']] = ProductSubCategorySerializer(ProductSubCategory.objects.filter(category_id=data['id']),many=True).data
        return data


    
    
