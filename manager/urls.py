from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', categories, name='category_detail'),
    path('product/<int:product_id>/', products, name='product_detail')
]