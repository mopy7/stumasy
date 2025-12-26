from rest_framework import serializers
from attendance.models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.user.get_full_name', read_only=True)
    marked_by_name = serializers.CharField(source='marked_by.get_full_name', read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'date', 'student', 'student_name', 'class_obj', 'status', 'marked_by', 'marked_by_name', 'created_at']
