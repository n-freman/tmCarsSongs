from django.urls import path
from rest_framework import routers
from singers.viewsets import SingersViewSet

from songs.viewsets import SongsViewSet

router = routers.DefaultRouter()
router.register(r'songs', SongsViewSet)
router.register(f'singer', SingersViewSet)

urlpatterns = router.urls

