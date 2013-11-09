# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('mgmeckern.apps.api.urls', namespace='api_v1')),
)

urlpatterns += i18n_patterns('',
    url(r'^', include('mgmeckern.apps.public.urls', namespace='public')),
)