from django.shortcuts import render
from .model.product import Product

def index(request):
    prod = Product.get_all_products()
    return render(request, 'index.html', {'products':prod})

