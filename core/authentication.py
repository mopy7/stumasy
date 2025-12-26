from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.db import connection

class TenantAwareJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # 1. Standard JWT authentication (decodes token, finds user)
        # Note: This finds the user IN THE CURRENT SCHEMA.
        # If schema is 'school2', it looks for User with id in token in 'school2'.
        
        user_auth_tuple = super().authenticate(request)
        
        if user_auth_tuple is None:
            return None
            
        user, token = user_auth_tuple
        
        # 2. Extract schema from token
        # We assume the token generation process adds 'schema_name' to the payload.
        token_schema = token.get('schema_name')
        
        if not token_schema:
            # Fallback or strict fail? Strict fail for safety.
            raise AuthenticationFailed("Token missing schema claim. Cannot verify tenant isolation.")
            
        # 3. Compare with current request schema
        current_schema = connection.schema_name
        
        if token_schema != current_schema:
            raise AuthenticationFailed(
                f"Cross-tenant access denied. Token for '{token_schema}' cannot be used on '{current_schema}'."
            )
            
        return user, token
