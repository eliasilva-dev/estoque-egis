from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import CreateUserView

# router = DefaultRouter()

# router.register('register', CreateUserView.as_view())
#router.register('users', UserViewSet)



urlpatterns = [
    path('user/register/', CreateUserView.as_view(), name="register")

]


