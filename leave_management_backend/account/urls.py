from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api

urlpatterns =[
    
    path('signup/', api.signup, name='signup'),
    # TokenObtainPairView will return a token to frontend 
    # after successful login as response.data
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]