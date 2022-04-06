from django.contrib import admin
from store.models import Product, ProductCategory, Variant, VariantOption, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Variant)
admin.site.register(Category)
admin.site.register(VariantOption)
