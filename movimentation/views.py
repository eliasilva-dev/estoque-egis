from django.shortcuts import render
from user.authentication import CookieJWTAuthentication
from rest_framework import viewsets, permissions
from movimentation.models import Movimentation_type, Movimentations
from movimentation.serializers import MovimentationSerializer, MovimentationTypeSerializer

class MovimentationViewSet(viewsets.ModelViewSet):
    

    permission_classes = [permissions.IsAuthenticated]

    authentication_classes = [CookieJWTAuthentication]

    queryset = Movimentations.objects.all()
    serializer_class = MovimentationSerializer



class MovimentaionTypeViewSet(viewsets.ModelViewSet):
    queryset = Movimentation_type.objects.all()
    serializer_class = MovimentationTypeSerializer


