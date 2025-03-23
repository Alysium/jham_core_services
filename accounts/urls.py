from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserDetailView

urlpatterns = [
    # API endpoints
    path('api/register/', UserRegistrationView.as_view(), name='api-register'),
    path('api/login/', UserLoginView.as_view(), name='api-login'),
    path('api/user/', UserDetailView.as_view(), name='api-user-detail'),
] 