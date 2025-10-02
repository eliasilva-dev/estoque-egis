from rest_framework.routers import DefaultRouter
from django.urls import path, include
from contract.views import ContractViewSet, ProposalViewSet, ListProposalViewSet, OnlyActiveContractViewSet

router = DefaultRouter()

router.register('contract', ContractViewSet)
router.register('contracts/active', OnlyActiveContractViewSet, basename='active-contract')
router.register('proposal', ProposalViewSet)
router.register('proposals/list', ListProposalViewSet, basename='list-proposal')



urlpatterns = [
    path('', include(router.urls))
]

