from rest_framework import viewsets
from classes.models import Class
from .serializers import ClassSerializer
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission

class IsSchoolAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.role == 'SCHOOL_ADMIN')

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated, IsSchoolAdminOrReadOnly]
