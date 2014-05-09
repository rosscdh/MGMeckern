# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

from mgmeckern.apps.report.forms import ReportForm

register = template.Library()


@register.inclusion_tag('report/map.html', takes_context=True)
def report_map(context, map_selector, callback='window.map_init_basic'):

    context.update({
        'map_selector': map_selector,
        'map_init_callback': callback,
        'report_form': ReportForm(),
        #'report_api_url': '/api/v1/report/',
        'report_api_url': reverse('report:create'),
    })

    if 'map_name' not in context:
        context['map_name'] = 'mg_meckern'

    return context