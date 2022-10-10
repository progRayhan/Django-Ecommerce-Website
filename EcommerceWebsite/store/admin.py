from django.contrib import admin
from store.model.product import Product
from store.model.category import Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)