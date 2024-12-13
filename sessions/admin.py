from django.contrib import admin
from .models import Session, SessionInstance

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    search_fields = ['name', 'type']

@admin.register(SessionInstance)
class SessionInstanceAdmin(admin.ModelAdmin):
    list_display = ['session', 'date', 'time', 'price_per_session', 'max_occupancy']
    list_filter = ['session', 'date']
    search_fields = ['session__name', 'session__type']
