from django.shortcuts import render
from rest_framework import viewsets
from contract.models import Contract, Proposal
from contract.serializers import ContractSerializer, ProposalSerializer, ListProposalSerializer
# Create your views here.


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer



class ListProposalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ListProposalSerializer
