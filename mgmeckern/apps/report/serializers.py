# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.humanize.templatetags.humanize import naturaltime

from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
#from drf_extra_fields.geo_fields import PointField

from .models import Report

import logging
import markdown2

logger = logging.getLogger('django.request')

MD = markdown2.Markdown()
BASE_URL = getattr(settings, 'BASE_URL', 'https://705837e4.ngrok.io')


class ReportSerializer(serializers.ModelSerializer):
    """
    used when GETing a report hides email and adds a few
    interesting fields
    """
    comment = serializers.SerializerMethodField()
    photo = Base64ImageField()
    # photo = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    date_modified = serializers.SerializerMethodField()

    lat = serializers.DecimalField(coerce_to_string=False, max_digits=22, decimal_places=19)
    lon = serializers.DecimalField(coerce_to_string=False, max_digits=22, decimal_places=19)

    css_severity = serializers.CharField(read_only=True, required=False)
    display_severity = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = Report
        exclude = ('email', 'points', 'is_deleted')

    def get_comment(self, obj):
        return mark_safe(MD.convert(obj.comment))

    def get_date_created(self, obj):
        return naturaltime(obj.date_created)

    def get_date_modified(self, obj):
        return naturaltime(obj.date_modified)

    # def get_photo(self, obj):
    #     try:
    #         return '{BASE_URL}{path}'.format(BASE_URL=BASE_URL, path=obj.photo.url)
    #     except Exception as e:
    #         logger.error('get_photo could not: %s' % e)
    #         return None

    def get_thumbnail(self, obj):
        try:
            return '{BASE_URL}{path}'.format(BASE_URL=BASE_URL, path=obj.thumbnail.url)
        except Exception as e:
            logger.error('get_thumbnail could not: %s' % e)
            return obj.thumbnail


class CreateReportSerializer(serializers.ModelSerializer):
    """
    used when POSTing a report
    """
    photo = Base64ImageField()

    class Meta:
        model = Report
