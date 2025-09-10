from rest_framework import serializers
from movimentation.models import Movimentations, Movimentation_type

from user.serializers import UserSerializer






class MovimentationTypeSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Movimentation_type
        fields = '__all__'




class MovimentationSerializer(serializers.ModelSerializer):

    movimentation = MovimentationTypeSerializer()
    user = UserSerializer()
    item = serializers.CharField(source="item.serial_number")
    item_name = serializers.CharField(source="item.item")
    
    class Meta:
        model = Movimentations  
        fields = ['id', 'item', 'item_name', 'movimentation', 'date', 'local', 'user', 'observation']
