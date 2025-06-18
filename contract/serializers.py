from rest_framework import serializers
from contract.models import Contract, Proposal


class ContractSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Contract
        fields = '__all__'


class ProposalSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Proposal
        fields = '__all__'