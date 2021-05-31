from django.db import models

# Create your models here.
from django.db import models
from embed_video.fields import EmbedVideoField


class stand_up(models.Model):
    video = EmbedVideoField(blank=True)


class sport(models.Model):
    video = EmbedVideoField(blank=True)


class motivation(models.Model):
    video = EmbedVideoField(blank=True)
