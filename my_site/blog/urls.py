from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="Starting-Page"),
    path("posts", views. posts, name="Posts-Page"),
    path("posts/<slug:slug>", views.post_detail, name="Post-Detail-page")
]
