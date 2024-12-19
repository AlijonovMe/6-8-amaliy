from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name')
    list_per_page = 10
    search_fields = ('id', 'name')
    actions_on_top = False


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count', 'published', 'category', 'getPhoto')
    list_display_links = ('id', 'name')
    list_editable = ('price', 'count', 'published', 'category')
    list_filter = ('id', 'name')
    list_per_page = 10
    search_fields = ('id', 'name')
    actions_on_top = False

    def getPhoto(self, products):
        if products.image:
            return mark_safe(f'<img src="{products.image.url}" width="150px">')
        return "Mavjud emas!"

    getPhoto.short_description = "Surati"


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
