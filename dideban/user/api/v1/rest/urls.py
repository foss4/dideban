from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView,
)

from .views import UserChangePassword, UserProfile

urlpatterns = [
    path('profile/', UserProfile.as_view(), name='user_profile'),
    path('password/', UserChangePassword.as_view(), name='change_password'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
