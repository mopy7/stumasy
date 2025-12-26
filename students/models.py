from django.db import models
from django.conf import settings

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    roll_number = models.CharField(max_length=20)
    current_class = models.ForeignKey('classes.Class', on_delete=models.SET_NULL, null=True, related_name='students')
    
    def __str__(self):
        return f"{self.user.username} ({self.roll_number})"
