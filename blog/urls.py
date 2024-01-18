from django.urls import path

from .views import timeline_page, home_page


urlpatterns=[
    path('', home_page, name='home-page'),
    path('timeline', timeline_page, name='timeline-page'),
]