from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Event(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    liked_by = models.ManyToManyField(
        User,
        related_name='liked_event',
        blank=True
    )
    lat = models.FloatField("latitude", blank=True, null=True)
    long = models.FloatField("longtitude", blank=True, null=True)
    address = models.TextField()