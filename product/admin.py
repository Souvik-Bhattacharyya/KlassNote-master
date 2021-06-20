from django.contrib import admin
from django.utils.html import format_html
from . import models


class ProductInline(admin.StackedInline):
    def thumbnail(self, obj):
        return format_html(f"<img src='{obj.thumbnail.image.url}' style='width: 240px; height: 240px; object-fit: scale-down;' />")

    def goto_product_details(self, obj):
        return format_html(f"<a href='/admin/product/product/{obj.id}/change/'>Details</a>")

    model = models.Product
    extra = 0
    fields = ['thumbnail', ('name', 'price', 'goto_product_details')]
    readonly_fields = ['thumbnail', 'goto_product_details']

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_delete_permission(self, *args, **kwargs):
        return False


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'number_of_products']
    fields = ['name', 'number_of_products']
    readonly_fields = ['number_of_products']
    inlines = [ProductInline]


class ProductImageInline(admin.TabularInline):
    def thumbnail(self, obj):
        return format_html(f"<img src='{obj.image.url}' style='width: 240px; height: 240px; object-fit: scale-down;' />")

    model = models.ProductImage
    fields = ['thumbnail', 'image']
    readonly_fields = ['thumbnail']
    extra = 0


class ProductSpecificationInline(admin.TabularInline):
    model = models.ProductSpecification
    extra = 0


class RelatedProductInline(admin.TabularInline):
    def thumbnail(self, obj):
        return format_html(f"<img src='{obj.related.thumbnail.image.url}' style='width: 240px; height: 240px; object-fit: scale-down;' />")

    def goto_details_page(self, obj):
        return format_html(f"<a href='/admin/product/product/{obj.related.id}/change/'>Details</a>")

    model = models.RelatedProduct
    extra = 0
    fields = ['thumbnail', 'related', 'goto_details_page']
    readonly_fields = ['thumbnail', 'goto_details_page']

    fk_name = 'product'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    list_filter = ['category']
    search_field = ['name', 'category__name', 'price', 'description']
    inlines = [ProductImageInline,
               ProductSpecificationInline, RelatedProductInline]


admin.site.register(models.ProductCategory, ProductCategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
