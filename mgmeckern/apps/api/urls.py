# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from mgmeckern.apps.report.views import ReportViewSet, DeletedReportViewSet
from mgmeckern.apps.public.api.views import AccountViewSet

router = routers.DefaultRouter()

router.register(r'report/deleted', DeletedReportViewSet)
router.register(r'report', ReportViewSet)
router.register(r'account', AccountViewSet)


urlpatterns = [
    url(r'^token/$', obtain_auth_token, name='auth_token'),
    url(r'^', include(router.urls)),
]