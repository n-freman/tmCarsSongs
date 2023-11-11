from rest_framework import permissions, viewsets

from .models import Song
from .serializers import SongSerializer


class SongsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    permission_classes = [permissions.IsAdminUser]

