from django.db import models


class Singer(models.Model):
    full_name = models.CharField(
        max_length=120,
        unique=True
    )
    image = models.ImageField(
        upload_to='singers',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.full_name

