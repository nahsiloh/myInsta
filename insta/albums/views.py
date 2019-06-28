from django.shortcuts import render
from django.contrib.auth.mixins import(LoginRequiredMixin)
from django.views.generic import (CreateView, UpdateView,
                                    DeleteView, ListView,
                                    DetailView)
from django.urls import reverse_lazy
from django.utils.text import slugify


# from braces.views import SelectRelatedMixin

from .forms import AlbumForm
from .models import Album
from images.models import Images

# Create your views here.


class CreateAlbumView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm


class ListAlbumView(LoginRequiredMixin, ListView):
    model = Album

    def get_queryset_album_images(self):
        return image.album_images.count()


class UpdateAlbumView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    redirect_field_name = 'albums/album_detail.html'
    template_name = "albums/album_update_form.html"



class DeleteAlbumView(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('albums:album_list')


class DetailAlbumView(LoginRequiredMixin, DetailView):
    model = Album
    # context_object_name = 'album_images'

    # def get_queryset(self):
    #     print (self.kwargs.get('slug'))
    #     a = Album.objects.get(slug=self.kwargs.get("slug"))
        # all_images = Images.objects.all()
        # return Images.objects.filter(album__name="{Album.name}")
        # return Images.objects.filter(album__name= a)

    # def get_object(self, queryset=None):
    #     slug = self.kwargs['slug']
    #     a_obj = Album.objects.get(slug=slug)
    #     try:
    #         i_obj = Images.objects.get(album=a_obj)
    #     except Images.DoesNotExist:
    #         d_obj = None
    #     except Images.MultipleObjectsReturned:
    #         return d_obj

    # def get_context_data(self, **kwargs):
    #     # xxx will be available in the template as the related objects
    #     context = super(DetailAlbumView, self).get_context_data(**kwargs)
    #     context['images_in_album'] = Images.objects.filter(album__name="{Album.name}")
    #     return context
