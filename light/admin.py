from django.contrib import admin
from .models import Light

class LightAdmin(admin.ModelAdmin):
    list_display = ["id", "color", "activate"]

admin.site.register(Light, LightAdmin)