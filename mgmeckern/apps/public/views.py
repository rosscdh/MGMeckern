# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from mgmeckern.apps.report.models import Report


class PublicHomeView(TemplateView):
    template_name = 'public/home.html'

    def get_context_data(self, **kwargs):
        context = super(PublicHomeView, self).get_context_data(**kwargs)
        context.update({
            'reports': Report.objects.all(),
        })
        return context