from django.urls import path

from .views import (timeline_page, home_page, create_post, 
    update_like, add_comment)


urlpatterns=[
    path('', home_page, name='home-page'),
    path('timeline', timeline_page, name='timeline-page'),
    path('create-post', create_post, name='create-post'),
    path('update-like', update_like, name='update-like'),
    path('add-comment/<int:post_id>', add_comment, name='add-comment'),
]