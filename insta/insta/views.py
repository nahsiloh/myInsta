from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader

from django.views.generic import (ListView)


from django.shortcuts import render

from images.models import Images
from images import forms


class HomePageView(ListView):
    model = Images
    template_name = 'index.html'

    def my_view(request):
        myimages = Images.objects.all()
        for entry in myimages:
            publish_status = entry.get_publish_display()
        return publish_status
