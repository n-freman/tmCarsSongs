from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Singer


class SingerAdminConfig(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'photo', 'songs_count']
    search_fields = ['full_name']

    def photo(self, obj):
        return mark_safe(f'''
        <img src={obj.image.url} style="height: 50px;" />
        ''')

    def songs_count(self, obj):
        return obj.songs.count()


admin.site.register(Singer, SingerAdminConfig)

