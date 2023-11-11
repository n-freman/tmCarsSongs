from rest_framework import serializers

from .models import Singer


class SingerSerializer(serializers.ModelSerializer):
    songs_count = serializers.SerializerMethodField()

    class Meta:
        model = Singer
        fields = ['id', 'full_name', 'image', 'songs_count']

    def get_songs_count(self, obj):
        return obj.songs.count()

