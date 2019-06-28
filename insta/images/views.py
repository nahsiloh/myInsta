from django.shortcuts import render
from django.contrib.auth.mixins import(LoginRequiredMixin)
from django.views.generic import (CreateView, UpdateView,
                                    DeleteView, ListView,
                                    DetailView)
from django.urls import reverse_lazy, reverse
from django.contrib import messages


from albums.models import Album
from .forms import ImageForm
from .models import Images

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


class CreateImageView(LoginRequiredMixin, CreateView):
    model = Images
    form_class = ImageForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ListImageView(LoginRequiredMixin, ListView):
    model = Images


class UpdateImageView(LoginRequiredMixin, UpdateView):
    model = Images
    form_class = ImageForm
    # fields = ['album', 'title', 'description']
    redirect_field_name = 'images/image_detail.html'
    template_name = 'images/images_update_form.html'


class DeleteImageView(LoginRequiredMixin, DeleteView):
    model = Images
    success_url = reverse_lazy('albums:album_list')

    # def get_success_url(self, **kwargs):
    #     return reverse('albums:album_detail', kwargs={"slug": self.kwargs.get("slug")})


class DetailImageView(LoginRequiredMixin, DetailView):
    model = Images
