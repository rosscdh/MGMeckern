# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('mgmeckern.apps.api.urls', namespace='api_v1')),
    url(r'^', include('mgmeckern.apps.public.urls', namespace='public')),
)
