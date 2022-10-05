from django.urls import path
from .views import (

    ProductCategoryListViewAPI,
    TopCategoryProduct

)

urlpatterns = [

    path("",ProductCategoryListViewAPI.as_view({'get': 'list'}),name="product-category-list-view-api"),
    path("top-product/",TopCategoryProduct.as_view(),name="top-product")

]