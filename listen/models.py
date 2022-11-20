from django.db import models

# Create your models here.
class Listen(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()
    audio = models.FileField(null=True, upload_to='uploads/')

class Emotion(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()
    audio = models.FileField(null=True, upload_to='uploads/')

class Sound(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()
    audio = models.FileField(null=True, upload_to='uploads/')
