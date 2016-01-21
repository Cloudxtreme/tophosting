from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^privacy-policy/', TemplateView.as_view(template_name="pages/privacy_policy.html"), name='privacy_policy'),
    url(r'^contact-us/', TemplateView.as_view(template_name="pages/contact_us.html"), name='contact_us'),
    url(r'^terms-of-use/', TemplateView.as_view(template_name="pages/terms_of_use.html"), name='terms_of_use'),
    url(r'^go/(?P<hosting_slug>[-\w]+)/$', views.click, name='click'),
    url(r'^(?P<hosting_slug>[-\w]+)/$', views.review, name='review'),
]
