# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .views import CreateReportView


urlpatterns = [
    # create report POST view
    url(r'^out-of-bounds/$', TemplateView.as_view(template_name='report/out-of-bounds.html'), name='out_of_bounds'),
    url(r'^$', csrf_exempt(CreateReportView.as_view()), name='create'),
]