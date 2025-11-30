from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'order']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'serie_number', 'brand', 'category', 'selling_price', 'quantity']
    list_filter = ['brand', 'category', 'created_at']
    search_fields = ['title', 'serie_number', 'description']
    inlines = [ProductImageInline]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'order', 'created_at']
    list_filter = ['created_at']