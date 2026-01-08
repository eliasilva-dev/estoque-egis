print("invoice.urls foi lido")

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from invoice.views import InvoiceViewSet, InvoiceItemViewSet, InvoicetypeViewSet, ItemCatalogViewSet, InvoiceListReadOnly, NotRegisterInvoicesView, InvoiceItemReadViewSet, InvoiceItemNotRegisterViewSet, InvoiceStatsView


router = DefaultRouter()


router.register('invoices', InvoiceViewSet)

router.register('invoice/list', InvoiceListReadOnly, basename='invoice-list')
router.register('invoice/unregister', NotRegisterInvoicesView, basename='not-registered-invoices')
router.register('invoiceitem', InvoiceItemViewSet)
router.register('invoice/item/list', InvoiceItemReadViewSet, basename='invoice-item-list')
router.register('invoice/item/unregister', InvoiceItemNotRegisterViewSet, basename='unregister-itens')
router.register('invoicetypes', InvoicetypeViewSet)

router.register('catalog', ItemCatalogViewSet)
urlpatterns  = [
    path('', include(router.urls)),
    path('invoice/info/stats/', InvoiceStatsView.as_view(), name='invoice-stats')
]

