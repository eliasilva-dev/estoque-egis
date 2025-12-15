
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stock.views import StockViewSet, ItemCategoryViewSet, StatusItemViewSet, LocalViewSet, EquipamentTypeViewSet

router = DefaultRouter()

router.register('stock', StockViewSet)
router.register('locals', LocalViewSet)
router.register('categories', ItemCategoryViewSet)
router.register('equipament/type', EquipamentTypeViewSet)
router.register('status', StatusItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]