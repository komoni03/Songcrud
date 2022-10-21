from datetime import datetime
import uuid
from django.db import models


# Create your models here.

class Artiste(models.Model):
    """
    The Artiste class is a model that has an id, first_name, last_name, and age
    The id is a UUIDField, which is a unique identifier. 
    The first_name and last_name are CharFields, which are strings. 
    The age is an IntegerField, which is an integer. 
    The id is the primary key, which means it's the unique identifier for each Artiste. 
    The default value for the id is a random UUID. 
    The id is not editable, which means it can't be changed. 
    The Artiste class is a model, which means it's a table
    """
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name.__str__()

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

    def __str__(self) -> str:
        return self.title.__str__()


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
