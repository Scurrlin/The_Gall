from django.db import models

import math

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    thumbnail_url = models.URLField()
    playback_url = models.URLField(default='')
    duration_ms = models.IntegerField()
    duration_minutes = models.IntegerField(default=0)
    duration_seconds = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Convert duration_ms to minutes and seconds
        self.duration_minutes = math.floor(self.duration_ms / 1000 / 60)
        self.duration_seconds = math.floor((self.duration_ms / 1000) % 60)
        super().save(*args, **kwargs)