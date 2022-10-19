from datetime import datetime
import uuid
from django.db import models


# Create your models here.
class Artiste(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()


class Song(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    title = models.CharField(max_length=100)
    date_released = models.DateField(default=datetime.today())
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)


class Lyric(models.Model):
    """
    It creates a table called Lyric with a primary key of id,
    a content field of type TextField with a
    max length of 5000, and
    a foreign key of song_id that references the Song table.
    """
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    content = models.TextField(5000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
