from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('gm', 'gm'),
        ('pa', 'pa'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True, default='pa')
    gm = models.CharField(max_length=20, blank=True, null=True, default='None')

    def __str__(self):
        return self.username
    
    def clean(self):
        # Hash the password if it's set and not hashed yet
        if self.password and not self.password.startswith('$'):  # Check if password is plain text
            self.set_password(self.password)
        super().clean()

