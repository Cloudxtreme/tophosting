from django.conf.urls import patterns, url

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<hosting_slug>[-\w]+)/$', views.review, name='review'),
]
