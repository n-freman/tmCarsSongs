from rest_framework import permissions, viewsets

from .models import Singer
from .serializers import SingerSerializer


class SingersViewSet(viewsets.ModelViewSet):
    serializer_class = SingerSerializer
    queryset = Singer.objects.all()
    permission_classes = [permissions.IsAdminUser]

