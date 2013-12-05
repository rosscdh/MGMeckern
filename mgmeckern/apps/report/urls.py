# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import CreateReportView


urlpatterns = patterns('',
    # create report POST view
    url(r'^$', CreateReportView.as_view(), name='create'),
)