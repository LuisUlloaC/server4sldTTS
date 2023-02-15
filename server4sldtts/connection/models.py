from datetime import datetime
from django.db import models


def pathToData(instance, filename):
    return f'data/{instance.id}/{filename}'


class Audio(models.Model):
    text = models.TextField(max_length=2000, default="this is a test text")
    language = models.TextField(max_length=50, default='es')
    file_name = models.TextField(max_length=1000, default=str(datetime.now))
    path = models.FileField(upload_to=pathToData, default='data/')

    def __str__(self):
        return self.file_name