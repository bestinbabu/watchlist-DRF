from django.urls import include, path
from rest_framework.authtoken.views import ObtainAuthToken

from user_app.api.views import LogoutView, RegistrationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('login/',ObtainAuthToken.as_view(),name='login'),
    path('register/',RegistrationView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]


