from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        SUPERUSER = "SUPERUSER", "System Owner" # For Public Schema
        SCHOOL_ADMIN = "SCHOOL_ADMIN", "School Admin"
        TEACHER = "TEACHER", "Teacher"
        STUDENT = "STUDENT", "Student"

    role = models.CharField(
        max_length=50, 
        choices=Role.choices, 
        default=Role.STUDENT # Default safe
    )

    # Add any other fields like phone number etc.

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = self.Role.SUPERUSER
        super().save(*args, **kwargs)
