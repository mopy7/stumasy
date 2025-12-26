from django.db import transaction
from django.contrib.auth import get_user_model
from rest_framework import serializers
from students.models import Student

User = get_user_model()

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.get_full_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    class_name = serializers.CharField(source='current_class.name', read_only=True)

    # Writable fields for User creation
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    user_email = serializers.EmailField(source='user.email', write_only=True, required=False)

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'roll_number', 'current_class', 'class_name', 'username', 'password', 'first_name', 'last_name', 'user_email']

    def create(self, validated_data):
        # Extract user data
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        email = validated_data.pop('user', {}).get('email', '')

        # Determine Role
        role = User.Role.STUDENT

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
            
            # 2. Create Student linked to User
            student = Student.objects.create(user=user, **validated_data)
        
        return student
