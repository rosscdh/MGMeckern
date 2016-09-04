# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils import translation
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.contrib.gis.geos import GEOSGeometry

from templated_email import send_templated_mail

from .models import Report

import logging
import django_rq
logger = logging.getLogger('django.request')

NAME, FROM_EMAIL = settings.ADMINS[0]
USE_EMAIL_QUEUE = getattr(settings, 'USE_EMAIL_QUEUE', False)


def send_mailout(report, from_email, recipients, language):
    translation.activate(getattr(settings, 'LANGUAGE_CODE', 'en'))

    send_templated_mail(template_name='new_report',
                        from_email=from_email,
                        recipient_list=[email for name, email in recipients],
                        context={
                            'email': report.email,
                            'comment': report.comment,
                            'address': report.address,
                            'severity': report.display_severity,
                            'lat': report.lat,
                            'lon': report.lon,
                            'date_created': report.date_created,
                            'date_modified': report.date_modified,
                        })


@receiver(post_save, sender='report.Report', dispatch_uid='report.on_new_report')
def on_new_report(sender, **kwargs):
    is_new = kwargs.get('created')
    report = kwargs.get('instance')
    language = translation.get_language()

    if is_new is True:

        if USE_EMAIL_QUEUE is False:
            send_mailout(report, FROM_EMAIL, settings.MANAGERS, language)

        else:

            try:
                django_rq.enqueue(send_mailout, report, FROM_EMAIL, settings.MANAGERS, language)
            except Exception as e:
                logger.error('An Exception occurred trying to send email asynchronously: %s' % e)
                # send locally
                send_mailout(report, FROM_EMAIL, settings.MANAGERS, language)


@receiver(pre_save, sender='report.Report', dispatch_uid='report.on_new_report.set_point')
def set_report_point_field(sender, **kwargs):
    report = kwargs.get('instance')
    if not report.points \
       and report.lat and report.lon:
        logger.info('saving geomerty for report: {lat}, {lon}'.format(lat=report.lat,
                                                                      lon=report.lon))

        report.points = GEOSGeometry('POINT({lon} {lat})'.format(lat=report.lat,
                                                                 lon=report.lon))
