from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import (
    Product,
    ProductCategory,
    ProductSubCategory
)
from .serializers import (
    ProductSerializer,
    ProductCategorySerializer,
    ProductSubCategorySerializer

)

class ProductCategoryListViewAPI(viewsets.ViewSet):
    
    def list(self, request):
        queryset = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(queryset, many=True)
        content = {
            "status":status.HTTP_200_OK,
            "success":True,
            "response":serializer.data
        }
        return Response(content,status=status.HTTP_200_OK)


class TopCategoryProduct(APIView):
    def get(self, request, *args, **kwargs):
        product_instance = set(Product.objects.all().values_list("product_category",flat=True))
        product_sub_category_instance = ProductSubCategory.objects.filter(id__in=list(product_instance))
        serializer = ProductSubCategorySerializer(product_sub_category_instance,many=True)
        content = {
            "status":status.HTTP_200_OK,
            "success":True,
            "response":serializer.data
        }
        return Response(content,status=status.HTTP_200_OK)



