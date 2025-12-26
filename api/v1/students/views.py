from rest_framework import viewsets
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsSchoolAdmin

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsSchoolAdmin]
