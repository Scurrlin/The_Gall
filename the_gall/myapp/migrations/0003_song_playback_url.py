# Generated by Django 5.0 on 2024-06-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_song_duration_minutes_song_duration_seconds"),
    ]

    operations = [
        migrations.AddField(
            model_name="song",
            name="playback_url",
            field=models.URLField(default=""),
        ),
    ]
