from rest_framework import serializers
from movimentation.models import Movimentations, Movimentation_type



class MovimentationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movimentations  
        fields = '__all__'


class MovimentationTypeSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Movimentation_type
        fields = '__all__'