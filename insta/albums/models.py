import datetime

from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    album_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Album, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('albums:album_detail', kwargs={"slug": self.slug})


    # @classmethod
    # def album_count(Album):
    #     no_of_albums = Album.objects.count()
    #     if no_of_albums == 0:
    #         return



    class Meta:
        ordering = ['-album_date']
