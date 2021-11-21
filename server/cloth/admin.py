from django.contrib import admin
from server.cloth.models import Clothes, Category, Attribute
from django.utils.html import format_html

# Register your models here.
@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    # def product_cover_thumbnail(self, obj):
    #     return format_html('<img src="{}" width="50px;"/>'.format(obj.image))

    # product_cover_thumbnail.short_description = "Thumbnail"
    list_display = (
        "id",
        # "product_cover_thumbnail",
        "image",
        "member",
        "color",
        "category",
        # "attributes",
    )
