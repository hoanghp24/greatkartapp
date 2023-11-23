from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.
class CartItemAdmin(admin.TabularInline):
    model = CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')
    inlines = [CartItemAdmin]



admin.site.register(Cart, CartAdmin)
