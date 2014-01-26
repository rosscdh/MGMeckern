# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from easy_thumbnails.files import get_thumbnailer

from . import SEVERITY_CHOICES
from .managers import ReportManager

import os


def _report_upload_path(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'report/%s-%s-%s%s' % (slugify(instance.email), instance.lat, instance.lon, ext)


class Report(models.Model):
    """
    User report model used to store the actual report
    """
    email = models.EmailField(_('Email'))
    comment = models.TextField(_('Comment'), help_text=_('Your review of the problem'))
    address = models.CharField(_('Address'), max_length=255, blank=True)
    severity = models.IntegerField(_('Severity'), help_text=_('How bad is the problem?'))
    lat = models.DecimalField(max_digits=22, decimal_places=19)
    lon = models.DecimalField(max_digits=22, decimal_places=19)
    photo = models.ImageField(upload_to=_report_upload_path, blank=True)

    date_created = models.DateTimeField(auto_now=False, auto_now_add=True, db_index=True)
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=True, db_index=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    is_public = models.BooleanField(default=False, db_index=True)
    photo_is_public = models.BooleanField(default=False, db_index=True)

    objects = ReportManager()

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return u'{comment} @ {address}'.format(comment=self.comment, address=self.address if self.address not in [None, ''] else self.latlng )

    @property
    def latlng(self):
        return (self.lat, self.lon)

    @property
    def photo_url(self):
        if self.photo_is_public is False:
            return '//placehold.it/75x75'
        else:
            thumbnail_options = {'crop': True, 'size': (75, 75)}
            thumbnailer = get_thumbnailer(self.photo)
            return thumbnailer.get_thumbnail(thumbnail_options).url

    @property
    def display_severity(self):
        return SEVERITY_CHOICES.get_desc_by_value(self.severity)

    @property
    def css_severity(self):
        """
        @TODO should be template tag
        """
        if SEVERITY_CHOICES.critical == self.severity:
            return 'label-danger'
        elif SEVERITY_CHOICES.bad == self.severity:
            return 'label-warning'
        else:
            return 'label-info'


"""
Import the signals
"""
from .signals import on_new_report