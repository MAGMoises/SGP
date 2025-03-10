from django.contrib import admin
from .models import Brand, Category, Product

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
  list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
  search_fields = ('name', 'description',)
  list_filter = ('is_active',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
  search_fields = ('name', 'description',)
  list_filter = ('is_active',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('title','brand', 'category', 'price',
                  'is_active', 'created_at', 'updated_at')
  search_fields = ('title','brand__name', 'category__name')
  list_filter = ('is_active', 'brand', 'category')

  

                

