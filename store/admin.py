from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery
import admin_thumbnails
from django.utils.html import format_html

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline, VariationInline]
    def thumbnail(self, obj):
        return format_html('<img src="{}" width="30" style="border-radius:50%">'.format(obj.images.url))


admin.site.register(Product, ProductAdmin)
admin.site.register(ReviewRating)
