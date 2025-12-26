from rest_framework import permissions

class IsSchoolAdmin(permissions.BasePermission):
    """
    Allows access only to School Admins.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'SCHOOL_ADMIN')

class IsTeacher(permissions.BasePermission):
    """
    Allows access only to Teachers.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'TEACHER')

class IsStudent(permissions.BasePermission):
    """
    Allows access only to Students.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'STUDENT')
