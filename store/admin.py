from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from . import models
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):  # -> Any:
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({'collection__id': str(collection.id)})
        )
        return format_html('<a href="{}">{}</a>', url, collection.products_count)
        # return collection.products_count

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super().get_queryset(request).annotate(products_count=Count('product'))


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price", "inventory_status", 'collection_title']
    list_editable = ["unit_price"]
    ordering = ["unit_price"]
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "LOW"
        else:
            return "OK"


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership", "order"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name"]
    list_per_page = 10

    def order(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({'customer__id': str(customer.id)})
        )
        return format_html(
            '<a href="{}">{} Orders</a>', url, customer.order_set.count()
        )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["placed_at", 'payment_status', 'customer']
    ordering = ['placed_at']
    list_per_page = 10
    list_select_related = ['customer']
