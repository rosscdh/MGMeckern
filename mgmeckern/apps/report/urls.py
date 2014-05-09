# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import CreateReportView


urlpatterns = patterns('',
    # create report POST view
    url(r'^out-of-bounds/$', TemplateView.as_view(template_name='report/out-of-bounds.html'), name='out_of_bounds'),
    url(r'^$', CreateReportView.as_view(), name='create'),
)