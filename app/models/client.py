import uuid
from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for each appointment
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)

