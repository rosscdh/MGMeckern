# -*- coding: utf-8 -*-
from django import template

from mgmeckern.apps.report.models import Report
from mgmeckern.apps.report.forms import AddressSearchForm, ReportForm

register = template.Library()


@register.inclusion_tag('report/map.html', takes_context=True)
def report_map(context):

    context.update({
        'search_form': AddressSearchForm(),
        'report_form': ReportForm(),
        'report_api_url': '/api/v1/report/',
        'pins': Report.objects.all(),
    })

    if 'map_name' not in context:
        context['map_name'] = 'mg_meckern'

    return context