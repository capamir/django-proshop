from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'isPaid', 'totalPrice', 'createdAt')
    raw_id_fields = ('user',)
    search_fields = ('user', 'totalPrice')
    list_filter = ('isPaid',)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'name',)
    raw_id_fields = ('order', 'product')
    search_fields = ('name',)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
