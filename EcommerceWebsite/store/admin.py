from django.contrib import admin
from store.model.product import Product
from store.model.category import Category

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category'] 

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category)