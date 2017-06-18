from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    
    # Include an application:
    # url(r'^app_name/', include('app_name.urls', namespace="app_name")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include("post.api.urls")),
)
