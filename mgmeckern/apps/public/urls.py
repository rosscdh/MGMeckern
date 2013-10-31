# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .views import PublicHomeView


urlpatterns = patterns('',
    # about
    url(r'^about/$', TemplateView.as_view(template_name='public/about.html'), name='about'),
    # home
    url(r'^$', PublicHomeView.as_view(), name='home'),
)