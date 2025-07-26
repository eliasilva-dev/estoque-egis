from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework import exceptions

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):    
        token = request.COOKIES.get("access_token")
        #print("Peguei o token:", token)
        if token is None:
            return None
        try:
            
            validated_token = self.get_validated_token(token)

            #print("Token valido: ", validated_token)
            user = self.get_user(validated_token)
            return user, validated_token
        except TokenError as e:
            #print(f"Entrei na exception: {e}")
            return None
        except exceptions.AuthenticationFailed as e:
           # print("Outro erro de autentificação:", e)
            return None
        except Exception as e:
           # print("Erro inesperado: ",e)
            return None
    
        
        
        
        # return self.get_user(validated_token), validated_token