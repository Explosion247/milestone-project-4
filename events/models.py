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
    embeded_map = models.TextField(default='Please insert HTML for an embeded google map' )
    event_date = models.DateTimeField(default=timezone.now)
    address = models.TextField()
    lat = models.FloatField("latitude", blank=True, null=True)
    long = models.FloatField("longitude", blank=True, null=True)
    liked_by = models.ManyToManyField(
        User,
        related_name='liked_event',
        blank=True
    )
    updated_at = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-updated_at"]


class Comment(models.Model):

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    content = models.TextField()
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="replies",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_at"]
