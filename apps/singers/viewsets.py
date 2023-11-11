from rest_framework import viewsets
from rest_framework import permissions

from .models import Singer
from .serializers import SingerSerializer


class SingersViewSet(viewsets.ModelViewSet):
    serializer_class = SingerSerializer
    queryset = Singer.objects.all()
    permission_classes = [permissions.IsAdminUser]

