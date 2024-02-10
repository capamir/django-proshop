from django.contrib import admin
from .models import Product, Review

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating', 'numReviews')
    raw_id_fields = ('user',)
    search_fields = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'rating', 'created')
    raw_id_fields = ('user', 'product')
    search_fields = ('name',)