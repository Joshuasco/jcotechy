from django.urls import path
from . import views

app_name = "product"

urlpatterns=[
path('', views.Products.as_view(), name='products'),
path('<slug>', views.ProductDetails.as_view(), name='product_details'),
path('search', views.productSearch, name='search' ),
]