# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from mgmeckern.apps.report.models import Report

from rest_framework.renderers import JSONRenderer
from mgmeckern.apps.report.serializers import ReportSerializer


class PublicHomeView(TemplateView):
    template_name = 'public/home.html'

    def get_context_data(self, **kwargs):
        context = super(PublicHomeView, self).get_context_data(**kwargs)

        active_reports = Report.objects.active()

        context.update({
            'search_form': None,
            'reports': active_reports,
            'pins': [ReportSerializer(r).data for r in active_reports]
        })
        return context