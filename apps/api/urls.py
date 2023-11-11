from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from singers.viewsets import SingersViewSet

from songs.viewsets import SongsViewSet

router = routers.DefaultRouter()
router.register(r'songs', SongsViewSet)
router.register(f'singer', SingersViewSet)

urlpatterns = router.urls

# API auth endpoints
urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

