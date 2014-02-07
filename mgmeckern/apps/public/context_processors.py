# -*- coding: utf-8 -*-
from django.conf import settings

from mgmeckern.apps.report.forms import AddressSearchForm


def search_form(request):
    return {
        'search_form': AddressSearchForm()
    }
