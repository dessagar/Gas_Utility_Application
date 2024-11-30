from django.contrib import admin
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['service_type', 'status', 'created_at', 'updated_at', 'user']

admin.site.register(ServiceRequest, ServiceRequestAdmin)
