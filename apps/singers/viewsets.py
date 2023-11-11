from rest_framework import permissions, viewsets

from .filters import SingerFilter
from .models import Singer
from .serializers import SingerSerializer


class SingersViewSet(viewsets.ModelViewSet):
    serializer_class = SingerSerializer
    queryset = Singer.objects.all()
    permission_classes = [permissions.IsAdminUser]
    filterset_class = SingerFilter

