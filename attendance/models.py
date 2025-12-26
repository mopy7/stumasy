from django.db import models

from django.conf import settings

class Attendance(models.Model):
    class Status(models.TextChoices):
        PRESENT = 'PRESENT', 'Present'
        ABSENT = 'ABSENT', 'Absent'
        LATE = 'LATE', 'Late'
        EXCUSED = 'EXCUSED', 'Excused'

    date = models.DateField()
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='attendance_records')
    class_obj = models.ForeignKey('classes.Class', on_delete=models.CASCADE, related_name='attendance_log')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PRESENT)
    marked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    # marked_by could be SchoolAdmin too (via User?)
    # Prompt: "Teacher Can mark attendance... School Admin Can mark and edit".
    # Better to link to User to allow both. Maybe GENERIC relation? Or just User FK.
    # User is in 'core.User'.
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('date', 'student', 'class_obj')

    def __str__(self):
        return f"{self.date} - {self.student} - {self.status}"
