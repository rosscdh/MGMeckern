# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers

from mgmeckern.apps.report.views import ReportViewSet, DeletedReportViewSet


router = routers.DefaultRouter()

router.register(r'report/deleted', DeletedReportViewSet)
router.register(r'report', ReportViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]