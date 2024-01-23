from django.urls import path

from .views import (timeline_page, home_page, create_post, 
    update_like, add_comment, profile_page, handle_follow)


urlpatterns=[
    path('', home_page, name='home-page'),
    path('timeline', timeline_page, name='timeline-page'),
    path('create-post', create_post, name='create-post'),
    path('update-like', update_like, name='update-like'),
    path('handle-follow/<int:user_id>', handle_follow, name='handle-follow'),
    path('add-comment/<int:post_id>', add_comment, name='add-comment'),
    path('profile-page/<int:user_id>', profile_page, name='profile-page'),
]