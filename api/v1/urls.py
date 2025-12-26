from django.urls import path, include

urlpatterns = [
    path('teachers/', include('api.v1.teachers.urls')),
    path('students/', include('api.v1.students.urls')),
    path('classes/', include('api.v1.classes.urls')),
    path('attendance/', include('api.v1.attendance.urls')),
]
