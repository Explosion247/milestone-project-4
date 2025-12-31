from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Event(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    event_image = CloudinaryField('event_image', default='placeholder')
    hero_image = CloudinaryField('hero_image', default='placeholder')
    event_date = models.DateTimeField(default=timezone.now)
    address = models.TextField()
    lat = models.FloatField("latitude", blank=True, null=True)
    long = models.FloatField("longtitude", blank=True, null=True)
    liked_by = models.ManyToManyField(
        User,
        related_name='liked_event',
        blank=True
    )
    status = models.IntegerField(choices=STATUS, default=0)