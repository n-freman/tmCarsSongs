from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Song


class SongAdminConfig(admin.ModelAdmin):
    list_display = ['id', 'title', 'singer', 'genre', 'photo']
    search_fields = ['title', 'genre']

    def photo(self, obj):
        return mark_safe(f'''
        <img src={obj.image.url} style="height: 50px;" />
        ''')

admin.site.register(Song, SongAdminConfig)

