from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.db import connection

class TenantTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['schema_name'] = connection.schema_name
        token['role'] = user.role
        
        return token
