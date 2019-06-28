from django import forms

from . import models


class ImageForm(forms.ModelForm):
    # publish = forms.ChoiceField(widget=forms.RadioSelect(), required=True)

    class Meta:
        fields = ['album', 'title', 'image', 'description', 'publish']
        model = models.Images
    
