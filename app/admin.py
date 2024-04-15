from django.contrib import admin
from .models import Category, Product, Order, OrderItem, ShippingAddress, AboutUs

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_category', 'is_sub', 'slug')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'digital', 'ImageURL')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_order', 'complete', 'transaction_id')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added', 'get_total')

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'address', 'city', 'state', 'mobile', 'date_added')

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
