from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.get_full_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    class_name = serializers.CharField(source='current_class.name', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'roll_number', 'current_class', 'class_name']
