import django_filters

from .models import Singer


class SingerFilter(django_filters.FilterSet):

    class Meta:
        model = Singer
        fields = ['full_name']

