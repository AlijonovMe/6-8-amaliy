from django.shortcuts import render, get_object_or_404, get_list_or_404
from datetime import datetime
from .models import *


def index(request):
    context = {
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def categories(request, category_id):
    category = get_object_or_404(Categories, id=category_id)
    products = Products.objects.filter(category_id=category_id, published=True)
    context = {
        'categories': [category],
        'products': products,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def products(request, product_id):
    products = get_object_or_404(Products, id=product_id, published=True)
    context = {
        'product': products,
        'current_year': datetime.now().year
    }

    return render(request, 'detail.html', context)
