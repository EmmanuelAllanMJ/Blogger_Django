from django.urls import path

from . import views

urlpatterns = [
    path("",views.starting_page, name='starting-page'),
    path("post/",views.posts, name='posts-page'),
    path("post/<slug:slug>",views.post_details, name='post-detail-page')
]
