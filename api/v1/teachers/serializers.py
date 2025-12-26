from django.db import transaction
from django.contrib.auth import get_user_model
from rest_framework import serializers
from teachers.models import Teacher

User = get_user_model()

class TeacherSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.get_full_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    
    # Writable fields for User creation
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    user_email = serializers.EmailField(source='user.email', write_only=True, required=False) # Optional, can use generated email or passed one

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'phone', 'specialization', 'username', 'password', 'first_name', 'last_name', 'user_email']

    def create(self, validated_data):
        # Extract user data
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        email = validated_data.pop('user', {}).get('email', '') # Handle source='user.email'
        
        # Determine Role
        role = User.Role.TEACHER

        with transaction.atomic():
            # 1. Create User
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                role=role
            )
            
            # 2. Create Teacher linked to User
            teacher = Teacher.objects.create(user=user, **validated_data)
        
        return teacher
