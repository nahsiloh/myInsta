from django import forms

from . import models

class AlbumForm(forms.ModelForm):

    class Meta:
        fields = ['name', 'description', 'album_date']
        model = models.Album
