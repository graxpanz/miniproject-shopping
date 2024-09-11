from django.urls import path
from supproduct import views

urlpatterns=[
    path("",views.index),
    path("product/details/<int:id>",views.supproductDetail,name="productDetail"),
    path("products",views.supproducts)
]