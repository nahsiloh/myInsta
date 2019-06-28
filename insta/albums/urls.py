from django.contrib import admin
from django.urls import path

from . import views

app_name = "albums"

urlpatterns = [
    path('create/', views.CreateAlbumView.as_view(), name="create_album"),
    # path('detail/<album_slug>', views.DetailAlbumView.as_view(), name="album_detail"),
    path('detail/<slug:slug>', views.DetailAlbumView.as_view(), name="album_detail"),
    path('list', views.ListAlbumView.as_view(), name="album_list"),
    path('delete/<slug:slug>', views.DeleteAlbumView.as_view(), name="album_delete"),
    path('edit/<slug:slug>', views.UpdateAlbumView.as_view(), name="album_edit"),

]
