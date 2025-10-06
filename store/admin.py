from django.contrib import admin
from .models import Collection, Product, Customer

admin.site.register(Collection)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price"]
    list_editable = ["unit_price"]
    ordering = ["unit_price"]
    list_per_page = 10


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name"]
    list_per_page = 10
