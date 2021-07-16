from django.contrib import admin
from .models.product import Product
from .models.catagory import Catagory



class AdminProduct(admin.ModelAdmin):
    list_display = ['pname', 'price', 'catagory']


class Admincatagory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, AdminProduct)
admin.site.register(Catagory, Admincatagory)

