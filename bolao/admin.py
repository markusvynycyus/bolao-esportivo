from django.contrib import admin
from .models import Time

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
