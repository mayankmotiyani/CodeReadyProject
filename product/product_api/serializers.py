from rest_framework import serializers
from product.models import (
    Product,
    ProductCategory,
    ProductSubCategory
)


class SingleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    
    def to_representation(self,instance):
        data = super(SingleProductSerializer,self).to_representation(instance)
        return data

class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    product_url = serializers.SerializerMethodField()
    owner = serializers.StringRelatedField()
    product_category = serializers.CharField(source='product_category.subcategory')

    class Meta:
        model = Product
        fields = ['id','product_name','product_price','product_category','product_url','owner']

    def get_product_url(self,instance):
        return instance.get_absolute_url()
    
    def get_product_name(self,instance):
        self.product_name = instance.product_name + " by " + instance.owner.username
        return self.product_name


class ProductSubCategoryForProductCategorySerializer(serializers.ModelSerializer):
    """ this class of for ProductCategorySerializer """
    class Meta:
        model = ProductSubCategory
        fields = ['id','subcategory']

class ProductSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubCategory
        fields = ['id','subcategory']

    def to_representation(self,instance):
        data = super(ProductSubCategorySerializer,self).to_representation(instance)
        data[data['subcategory']] = ProductSerializer(Product.objects.filter(product_category_id=data['id']),many=True).data
        data['url'] = "/get-product/" + "product-category/" +  data['subcategory']
        return data


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id','category']

    def to_representation(self,instance):
        data = super(ProductCategorySerializer,self).to_representation(instance)
        data["category_list"] = ProductSubCategoryForProductCategorySerializer(ProductSubCategory.objects.filter(category_id=data['id']),many=True).data
        return data


    
    
