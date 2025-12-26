from rest_framework import viewsets, permissions, exceptions
from attendance.models import Attendance
from .serializers import AttendanceSerializer
from rest_framework.permissions import IsAuthenticated

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = Attendance.objects.all()
        
        if user.role == 'SCHOOL_ADMIN':
            return qs
        if user.role == 'TEACHER':
            # Teachers see attendance for classes they teach
            # Assuming Teacher model is linked to user
            if hasattr(user, 'teacher_profile'):
               return qs.filter(class_obj__teacher=user.teacher_profile)
            return qs.none() 
        if user.role == 'STUDENT':
             # Students see only their own
            if hasattr(user, 'student_profile'):
                return qs.filter(student=user.student_profile)
            return qs.none()
            
        return qs.none()

    def perform_create(self, serializer):
        user = self.request.user
        class_obj = serializer.validated_data['class_obj']
        
        # Validation: Only Teacher of the class (or Admin) can mark attendance
        if user.role == 'TEACHER':
            if not hasattr(user, 'teacher_profile') or class_obj.teacher != user.teacher_profile:
                 raise exceptions.PermissionDenied("You can only mark attendance for your own classes.")
        
        elif user.role != 'SCHOOL_ADMIN':
             raise exceptions.PermissionDenied("Only Teachers and Admins can mark attendance.")
             
        serializer.save(marked_by=user)
