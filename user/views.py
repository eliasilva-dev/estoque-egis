from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from user.serializers import UserSerializer
#from user.models import User


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


    


    