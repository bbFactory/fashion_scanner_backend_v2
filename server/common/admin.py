from django.contrib import admin
from server.common.models import Brand, Color


class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)

class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "hex_code",)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Color, ColorAdmin)
