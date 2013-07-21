from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

urlpatterns = patterns('website.views',
    url("^$", 'base', name="home"),
)
