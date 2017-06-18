from django.conf.urls import patterns, include, url
from .views import BlogPostAPIView

urlpatterns = patterns('',
    url(r'post/$', BlogPostAPIView.as_view()),
)
