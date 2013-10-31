# -*- coding: utf-8 -*-
from mgmeckern.utils import get_namedtuple_choices


SEVERITY_CHOICES = get_namedtuple_choices('SEVERITY_CHOICES', (
        (2, 'critical', 'Critical'),
        (1, 'bad', 'Bad'),
        (0, 'irritating', 'Irritating'),
))