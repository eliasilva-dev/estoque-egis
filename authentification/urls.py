from django.urls import path
from user.views import LoginView, isAuthView, RefreshTokenView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
    
)

urlpatterns = [
    # path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('auth/token/', LoginView.as_view(), name="login"),
    path('auth/token/refresh/', RefreshTokenView.as_view(), name="refresh-token"),
    path('auth/check/', isAuthView.as_view(), name="is-auth"),
    
    
]