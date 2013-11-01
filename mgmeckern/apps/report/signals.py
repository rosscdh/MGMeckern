# -*- coding: utf-8 -*-
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from templated_email import send_templated_mail

from .models import Report

import logging
logger = logging.getLogger('django.request')

NAME, FROM_EMAIL = settings.ADMINS[0]


@receiver(post_save, sender=Report, dispatch_uid='report.on_new_report')
def on_new_report(sender, **kwargs):
    is_new = kwargs.get('created')
    report = kwargs.get('instance')

    if is_new is True:

        send_templated_mail(
                template_name='new_report',
                from_email=FROM_EMAIL,
                recipient_list=[email for name, email in settings.MANAGERS],
                context={
                    'email': report.email,
                    'comment': report.comment,
                    'address': report.address,
                    'severity': report.display_severity,
                    'lat': report.lat,
                    'lon': report.lon,
                    'date_created': report.date_created,
                    'date_modified': report.date_modified,
                }
        )