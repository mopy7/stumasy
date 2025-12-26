from rest_framework import serializers
from teachers.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.get_full_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'phone', 'specialization']
