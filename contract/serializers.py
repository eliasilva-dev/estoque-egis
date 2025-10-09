from rest_framework import serializers
from contract.models import Contract, Proposal


class ContractSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format="%d/%m/%Y")
    end_date = serializers.DateField(format="%d/%m/%Y")
    class Meta: 
        model = Contract
        fields = ['id', 'number_contract', 'contract_name', 'start_date', 'end_date', 'is_active', 'was_delete']


class OnlyContractActiveSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    contract_name = serializers.CharField()
   



class ProposalSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Proposal
        fields = ['contract', 'number_proposal', 'description', 'is_registred']


class ListProposalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    contract = serializers.CharField()
    number_proposal = serializers.CharField()
    is_registred = serializers.BooleanField()
    description = serializers.CharField()
    was_delete = serializers.BooleanField()

