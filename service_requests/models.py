from django.db import models
from django.contrib.auth.models import User  # For the user field


from django.db import models

from django.db import models
from django.contrib.auth.models import User  # Assuming you are using the built-in User model

class ServiceRequest(models.Model):
    service_type = models.CharField(max_length=255)  # e.g., installation, repair, maintenance
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending')  # e.g., Pending, In Progress, Completed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update on each save
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_requests',  null=True, blank=True)  # Reference to User

    def __str__(self):
        return self.service_type

