from django.contrib import admin
from django.urls import path

from shop.views import index, product_detail,expensive_products

urlpatterns = [
    path('home/', index, name='home'),
    path('home/',index,name='hom'),
    path('category/<slug:category_slug>/products', index, name='products_of_category'),
    path('product_detail/<slug:slug>',product_detail,name='product_detail'),
    path('product_r/<slug:slug>products',product_detail,name='product_r'),
    path('exspensive/',expensive_products,name='exspensive_product'),
    ]