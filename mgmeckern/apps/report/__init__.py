# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from mgmeckern.utils import get_namedtuple_choices


SEVERITY_CHOICES = get_namedtuple_choices('SEVERITY_CHOICES', (
        (2, 'critical', _('Critical')),
        (1, 'bad', _('Bad')),
        (0, 'irritating', _('Irritating')),
))

REPORT_TYPE_CHOICES = get_namedtuple_choices('REPORT_TYPE_CHOICES', (
        (0, 'damage', _('Damage')),
        (1, 'improvement', _('Improvment')),
))