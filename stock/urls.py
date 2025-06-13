
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stock.views import StockViewSet, ItemCategoryViewSet

router = DefaultRouter()

router.register('stock', StockViewSet)
router.register('categories', ItemCategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]