from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status

from contract.models import Contract, Proposal
from contract.serializers import ContractSerializer, ProposalSerializer, ListProposalSerializer, OnlyContractActiveSerializer
# Create your views here.


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class OnlyActiveContractViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contract.objects.filter(is_active=True, was_delete=False)
    serializer_class = OnlyContractActiveSerializer


class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        proposal = serializer.save()

        response_serializer = ListProposalSerializer(proposal)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        proposal = serializer.save()

        response_serializer = ListProposalSerializer(proposal)

        return Response(response_serializer.data, status=status.HTTP_200_OK)
       
    
    



class ListProposalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ListProposalSerializer
