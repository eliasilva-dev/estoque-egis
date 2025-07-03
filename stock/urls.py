
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stock.views import StockViewSet, ItemCategoryViewSet, StatusItemViewSet

router = DefaultRouter()

router.register('stock', StockViewSet)
router.register('categories', ItemCategoryViewSet)
router.register('status', StatusItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]