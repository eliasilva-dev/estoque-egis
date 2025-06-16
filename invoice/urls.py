from django.urls import path, include
from rest_framework.routers import DefaultRouter

from invoice.views import InvoiceViewSet, Invoice_ItemViewSet, Invoice_typeViewSet


router = DefaultRouter()

router.register('invoice', InvoiceViewSet)
router.register('invoiceitens', Invoice_ItemViewSet)
router.register('invoicetypes', Invoice_typeViewSet)

urlpatterns  = [
    path('', include(router.urls))
]