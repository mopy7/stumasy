from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=50) # e.g. "Grade 10-A"
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True, related_name='assigned_classes')
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.name
