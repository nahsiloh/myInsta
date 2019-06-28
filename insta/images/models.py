import datetime

from django import forms
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse


from albums.models import Album
# from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Images(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, default='')
    upload_date = models.DateField(default=timezone.now)
    album = models.ForeignKey(Album, related_name='album_images',
        on_delete=models.CASCADE)

    PRIVATE ='PR'
    PUBLIC = 'PU'

    PUBLISH_CHOICES = [
            (PRIVATE, 'Private'),
            (PUBLIC, 'Public'),]
    publish = models.CharField(max_length=7,
                        choices=PUBLISH_CHOICES,
                        default=PRIVATE)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('albums:album_detail', kwargs={"slug": slugify(self.album)})




    class Meta:
        ordering = ['-upload_date']

    # @property
    # def image_publish(self):
    #     return self.get_publish_display()
