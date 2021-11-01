from django.contrib import admin
from server.member.models import Members

class MembersAdmin(admin.ModelAdmin):
    list_display = ("id", "ko_name", "en_name", "group_type", "color",)


admin.site.register(Members, MembersAdmin)
