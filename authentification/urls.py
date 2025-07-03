from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('authentification/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authentification/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authentification/token/verify/', TokenVerifyView.as_view(), name='token_verify')
    
]