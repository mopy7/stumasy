from rest_framework import viewsets
from teachers.models import Teacher
from .serializers import TeacherSerializer
from rest_framework.permissions import IsAuthenticated

class TeacherViewSet(viewsets.ModelViewSet):
    # Only allow listing/viewing? Or full CRUD? 
    # For now, full CRUD but permissions usually restricted.
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
