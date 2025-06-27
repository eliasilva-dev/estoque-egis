print("invoice.urls foi lido")

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from invoice.views import InvoiceViewSet, InvoiceItemViewSet, InvoicetypeViewSet, ItemCatalogViewSet


router = DefaultRouter()

router.register('invoice', InvoiceViewSet)
router.register('invoiceitem', InvoiceItemViewSet)
router.register('invoicetypes', InvoicetypeViewSet)
router.register('catalog', ItemCatalogViewSet)
urlpatterns  = [
    path('', include(router.urls))
]

