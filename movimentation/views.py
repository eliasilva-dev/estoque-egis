from django.shortcuts import render

from rest_framework import viewsets
from movimentation.models import Movimentation_type, Movimentations
from movimentation.serializers import MovimentationSerializer, MovimentationTypeSerializer

class MovimentationViewSet(viewsets.ModelViewSet):

    queryset = Movimentations.objects.all()
    serializer_class = MovimentationSerializer



class MovimentaionTypeViewSet(viewsets.ModelViewSet):
    queryset = Movimentation_type.objects.all()
    serializer_class = MovimentationTypeSerializer


