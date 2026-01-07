from rest_framework import serializers
from movimentation.models import Movimentations, Movimentation_type
from stock.models import Stock
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer


User = get_user_model()



class MovimentationTypeSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Movimentation_type
        fields = '__all__'




class MovimentationSerializer(serializers.ModelSerializer):

    item = serializers.PrimaryKeyRelatedField(queryset=Stock.objects.all())
    movimentation = serializers.PrimaryKeyRelatedField(queryset=Movimentation_type.objects.all())
    # usuário vem do contexto (não precisa enviar no payload)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Movimentations  
        fields = ['id', 'item', 'movimentation', 'date', 'local', 'user', 'observation']
