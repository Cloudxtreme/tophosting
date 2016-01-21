from django.contrib import admin

from .models import Hosting, Click

admin.site.register(Hosting)


class ClickAdmin(admin.ModelAdmin):
    list_display = ('hosting', 'ip', 'created_at')
admin.site.register(Click, ClickAdmin)
