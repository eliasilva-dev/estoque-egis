from rest_framework import viewsets
from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny, DjangoModelPermissions
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.response import Response
from user.serializers import UserSerializer
from django.contrib.auth import authenticate
#from user.models import User


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


    

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        #print(request.data)
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user: 
            print("Senha e user correto")
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            response = Response({"message": "Login Realizado"}, status=200)
            #to do: change the configuration of duration of access_token  
            response.set_cookie(
                key="access_token",
                value=str(refresh.access_token),
                httponly=True,
                secure=False,
                max_age=60,
                samesite="Lax",
                path="/",
            )

            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                secure=False,
                samesite="Lax",
                path="/"

            )
            return response
        return Response({"error:" "Credenciais inválidas"})
            

class LogoutView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        response = Response({"message": "Logout efetuado"}, status=200)
        print("Entrei no post")
        print("Antes do delete: ")
        print(response.cookies)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
       
        return response


class isAuthView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"authenticated": True})




class RefreshTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("Entrei na request do Refresh")
        refresh_token = request.COOKIES.get("refresh_token")
        print("Verifiquei o cookie")
        if not refresh_token:
            return Response({"error": "Refresh token not found"})
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            response = Response({"message": "Token was updated"}, status= 200)

            response.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                max_age=60,
                secure=False,
                samesite="Lax",
                path="/",
            )
            return response
        except TokenError:
            return Response({"error": "Refresh token invalid"})
    