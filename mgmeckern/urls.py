# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/v1/token-auth/', obtain_jwt_token),
    url(r'^api/v1/token-refresh/', refresh_jwt_token),

    url(r'^api/v1/', include('mgmeckern.apps.api.urls', namespace='api_v1')),

    url(r'^create/', include('mgmeckern.apps.report.urls', namespace='report')),
]

urlpatterns += [
    url(r'^', include('mgmeckern.apps.public.urls', namespace='public')),
]

if settings.DEBUG or settings.PROJECT_ENVIRONMENT == 'dev':
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
