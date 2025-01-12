import uuid
from django.db import models
from app.models import User
from app.models import Client

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('confirmed', 'confirmed'),
        ('completed', 'completed'),
        ('canceled', 'canceled'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pa_ref = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    gm_ref = models.CharField(max_length=20, default='null')
    appointment_date = models.DateTimeField(auto_now_add=True)  # Automatically sets current date & time if not provided
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for each appointment
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates when modified

    def __str__(self):
        return f"Appointment with {self.client} on {self.appointment_date}"

    class Meta:
        ordering = ['appointment_date']
