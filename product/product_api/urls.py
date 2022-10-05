from django.urls import path
from .views import (

    ProductCategoryListViewAPI,
    TopCategoryProduct,
    RetrieveProductByProductCategory,
    GetProductDetail

)

urlpatterns = [

    path("",ProductCategoryListViewAPI.as_view({'get': 'list'}),name="product-category-list-view-api"),
    path('product-detail/<slug:product_slug>/',GetProductDetail.as_view({'get': 'list'}),name="get-product-detail"),
    path("top-product/",TopCategoryProduct.as_view(),name="top-product"),
    path('product-category/<str:product_category_name>/',RetrieveProductByProductCategory.as_view(),name="product-category")
    # path("product/",)

]