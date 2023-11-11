from rest_framework import viewsets

from .models import Singer
from .serializers import SingerSerializer


class SingersViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SingerSerializer
    queryset = Singer.objects.all()

