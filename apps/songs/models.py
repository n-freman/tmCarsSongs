from django.db import models
from singers.models import Singer


class Song(models.Model):
    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE,
        related_name='songs'
    )
    title = models.CharField(max_length=120)
    image = models.ImageField(
        upload_to='songs',
        null=True,
        blank=True
    )
    genre = models.CharField(max_length=120)

    class Meta:
        unique_together = ('singer', 'title')

    def __str__(self):
        return f'{self.singer}: {self.title}'

