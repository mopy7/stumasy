from rest_framework import serializers
from classes.models import Class

class ClassSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.user.get_full_name', read_only=True)

    class Meta:
        model = Class
        fields = ['id', 'name', 'teacher', 'teacher_name', 'description']
