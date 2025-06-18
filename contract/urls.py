from rest_framework.routers import DefaultRouter
from django.urls import path, include
from contract.views import ContractViewSet, ProposalViewSet

router = DefaultRouter()

router.register('contract', ContractViewSet)
router.register('proposal', ProposalViewSet)

urlpatterns = [
    path('', include(router.urls))
]

