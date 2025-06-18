from rest_framework.routers import DefaultRouter
from django.urls import path, include
from movimentation.views import MovimentationViewSet, MovimentaionTypeViewSet

router = DefaultRouter()
router.register('movimentations', MovimentationViewSet)
router.register('movtypes', MovimentaionTypeViewSet)

urlpatterns = [
    path('', include(router.urls))
]