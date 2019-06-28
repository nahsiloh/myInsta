from django.contrib import admin
from django.urls import path

from . import views

app_name = "images"

urlpatterns = [
    path('post/', views.CreateImageView.as_view(), name="create_image"),
    path('<int:pk>/', views.DetailImageView.as_view(), name="detail_image"),
    path('<int:pk>/edit/', views.UpdateImageView.as_view(), name="edit_image"),
    path('<int:pk>/delete/', views.DeleteImageView.as_view(), name="delete_image"),


]
