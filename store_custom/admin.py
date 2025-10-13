from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from playground.views import Product
from store.admin import ProductAdmin
from tags.models import TaggedItem

# Register your models here.


class TagInline(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']
    min_num = 1
    max_num = 10
    extra = 0  # type: ignore


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
