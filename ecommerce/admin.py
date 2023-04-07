from django.contrib import admin
from .models import (
    ProductCat, Product, ProductImg, OrderProduct, 
    Order, Payment, Coupon, Refund
    )

##### REGISTER MODELS ####

@admin.register(ProductImg)
class ProductImgAdmin(admin.ModelAdmin):
    list_display = ['product', 'prodt_img','is_active']
    list_filter =['is_active','created_on']
    search_fields=['created_on','updated_on']
    readonly_fields=['created_on','updated_on']

@admin.register(ProductCat)
class ProductCatAdmin(admin.ModelAdmin):
    list_display = ['title', 'cat_img','is_active','created_on','updated_on']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields=['created_on','updated_on']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','seller', 'prodt_cat','prodtImg','price','discount_price','in_stock','is_active']
    prepopulated_fields = {'slug': ('title',)}
    list_editable=['discount_price','in_stock','is_active']
    list_filter=['in_stock','is_active']
    search_fields=['title','seller', 'product_cat', 'price','discount_price','created_on']
    search_help_text="search by 'title','seller', 'product_cat', 'price','discount_price' or 'created_on' fields"
    readonly_fields=['created_on','updated_on']

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'buyer', 'quantity','ordered']
    search_fields=['product','buyer','created_on']
    readonly_fields=['created_on','updated_on']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id','buyer','ordered', 'shipping_address','billing_address']
    list_filter=['created_on','ordered']
    search_fields=['order_id']
    search_help_text='search by order_id'
    readonly_fields=['created_on','updated_on']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['stripe_charge_id','buyer', 'amount','status','paid','timestamp']
    list_filter=['paid']
    search_fields=['date','buyer']
    search_help_text="search by date or buyer"
    readonly_fields=['timestamp']

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display=['code','amount','created_on']
    search_fields=['code','amount']
    list_filter=['created_on']
    search_help_text="search by code or amount"
    
@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display=['prodt_id','order_id','accepted','email']
    list_filter=['accepted']
    search_fields=['prodt_id','order_id']
    search_help_text="search by prodt_id or order_id"
    



