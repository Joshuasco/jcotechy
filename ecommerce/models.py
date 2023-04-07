import uuid
from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse
from django.utils.html import mark_safe, format_html
from tinymce.models import HTMLField
from account.models import Address
from django.contrib.auth.models import User




 ################ PRODUCTCAT MODEL ##################
 ################ PRODUCTCAT MODEL ##################
class ProductCatManager(models.Manager):
    def get_queryset(self):
        return super(ProductCatManager, self).get_queryset().filter(is_active=True)

class ProductCat(models.Model):
    title=models.CharField(max_length=50)
    slug = models.SlugField(default='')
    image=models.ImageField(upload_to='core/product/category_img')
    alt_text = models.CharField(max_length=50, help_text='enter an alternate text for this image', null=True, blank=True, default= '')
    is_active=models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    objects=models.Manager() #default ProductCat manager
    product_imgs=ProductCatManager() #custom ProductCat manager

    def __str__(self):
        return self.title

    def cat_img(self):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = self.image.url,
            width='50',height='50',
            )
    )
    
    


################ PRODUCT MODEL ##################
################ PRODUCT MODEL ##################
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)
    
class Product(models.Model):
    seller=   models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(default='')
    keywords = models.CharField(max_length=100, blank=True, null=True, help_text="enter comma separated words")
    prodt_cat= models.ForeignKey(ProductCat, on_delete=models.SET_NULL, null=True)
    prodt_img =models.ImageField(upload_to="ecommerce/product_img" )
    short_description = models.CharField( max_length=160, default='')
    description = HTMLField(default='')
    price = models.PositiveIntegerField(default=0)
    discount_price = models.PositiveIntegerField(default=0)
    available_qty= models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    is_active= models.BooleanField(default=True)
    created_on = models.DateTimeField(default=datetime.now)
    updated_on=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural='products'
        ordering= ('-created_on',)
    
    objects=models.Manager() #default product manager
    products=ProductManager() #custom product manager

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse( 'product:prodcuct_details', kwargs={'slug':self.slug})

    def prodtImg(self):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = self.prodt_img.url,
            width='50',height='50',
            )
    )


################ PRODUCTIMG MODEL ##################
################ PRODUCTIMG MODEL ##################
class ProductImgManager(models.Manager):
    def get_queryset(self):
        return super(ProductImgManager, self).get_queryset().filter(is_active=True)

class ProductImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    image=models.ImageField(upload_to='core/product/product_img')
    alt_text = models.CharField(max_length=50, help_text='enter an alternate text for this image', null=True, blank=True, default= '')
    is_active=models.BooleanField(default=True)
    created_on= models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)

    verbose_name = 'product'
    verbose_name_plural='products'
    ordering= ('-created_on',)

    objects=models.Manager() #default ProductCat manager
    product_cats=ProductCatManager() #custom ProductCat manager

    def __str__(self):
        return str(self.product)

    def prodt_img(self):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = self.image.url,
            width='50',height='50',
            )
    )
    
    


################ ORDERPRODUCT MODEL ##################
################ ORDERPRODUCT MODEL ##################

class OrderProduct(models.Model):
    buyer =  models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0)
    ordered=models.BooleanField(default=False)
    created_on = models.DateTimeField(default=datetime.now)
    updated_on=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural='products'
        ordering= ('-created_on',)

    def __str__(self):
        return str(self.product)

    def get_total_discount_price(self):
        total_discount_price=self.product.discount_price * self.quantity
        return total_discount_price

    def get_total_price(self):
        total_price=self.product.price * self.quantity
        return total_price
    
    def get_total_amount_saved(self):
        total_amount_saved=self.get_total_price - self.get_total_discount_price
        return total_amount_saved

    def get_final_price(self):
        if self.get_total_discount_price():
            return self.get_total_discount_price()
        return self.get_total_price


################ ORDER MODEL ##################
################ ORDER MODEL ##################

STATUS=[
    ('pending','pending'), #when orderProduct is created (items in cart)
    ('received','received'), #when order is placed after checkout
    ('processing','processing'), #order about to be shipped
    ('transit','transit'), #order in delevery
    ('confirmed','confirmed'), #order received and confirmed my buyer 
    ('canceled','canceled'), #orer canceled (late delivery or user request refund) 
]

class Order(models.Model):
    buyer =  models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=20, blank=True, null=True)
    order_products= models.ManyToManyField(OrderProduct)
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        Address, related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        Address, related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True) 
    created_on = models.DateTimeField(default=datetime.now)
    updated_on=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural='products'
        ordering= ('-created_on',)

    def __str__(self):
        return self.order_id

    def get_total_price(self):
        for prodt in self.order_products:
            total_price += prodt.get_final_price()
        return total_price


################ PAYMENT MODEL ##################
################ PAYMENT MODEL ##################
PAYMENT_STATUS=[
    ('PENDING','PENDING'),
    ('FAILED','FAILED'),
    ("SUCCESSFULL", "SUCCESSFULL")
]
class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    buyer = models.ForeignKey(User,  on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    status=models.CharField(choices=PAYMENT_STATUS, default="PENDING", max_length=12)
    paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.paid


################ COUPON MODEL ##################
################ COUPON MODEL ##################

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()
    created_on= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code


################ REFUND MODEL ##################
################ REFUND MODEL ##################

class Refund(models.Model):
    order_id = models.CharField(max_length=15)
    prodt_id=models.CharField(max_length=15)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.order_id}"

         
