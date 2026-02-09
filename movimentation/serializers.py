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
        fields = [
            'id',
            'item',
            'movimentation',
            'moviment_flow',
            'previous_status',
            'new_status',
            'date',
            'local',
            'user',
            'observation'
        ]





# class MovimentationCreateSerializer(serializers.ModelSerializer):

#     class Meta: 
#         model = Movimentations
#         fields = [
#             'item', 'movimentation', 'moviment_flow', 'local', 'observation'
#         ]
    


#     def create(self, validated_data):
#         stock = validated_data['item']
#         movimentation_type = validated_data['movimentation_type']

#         previsous_status = stock.status
#         new_status = self._resolve_new_status(movimentation_type)

#         moviment = Movimentations.objects.create(
#             previsous_status=previsous_status,
#             new_status = new_status,
#             user=self.context['request'].user,
#             **validated_data
#         )

#         stock.status = new_status
#         stock.local = validated_data['local']
#         stock.save()

#         return moviment
    
#     def _resolve_new_status(self, movimentation_type):

#         code = movimentation_type.code

       