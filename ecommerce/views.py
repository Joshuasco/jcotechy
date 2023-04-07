from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import (
    ProductCat, Product, ProductImg, OrderProduct, 
    Order, Payment, Coupon, Refund
    )
# Create your views here.
class Products(ListView):
    model=Product
    template_name='core/product.html'
    context_object_name = 'projects'
    queryset= Product.products.all()


class ProductDetails(DetailView):
    model=Product
    template_name='ecommerce/product_details.html'
    context_object_name = 'product'


def productSearch(self):
    pass