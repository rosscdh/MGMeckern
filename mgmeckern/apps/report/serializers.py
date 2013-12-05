# -*- coding: utf-8 -*-
from django.conf import settings
from rest_framework import serializers

from easy_thumbnails.files import get_thumbnailer

from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    """
    used when GETing a report hides email and adds a few 
    interesting fields
    """
    photo = serializers.SerializerMethodField('get_photo')
    css_severity = serializers.CharField(source='css_severity', read_only=True, required=False)
    display_severity = serializers.CharField(source='display_severity', read_only=True, required=False)

    class Meta:
        model = Report
        exclude = ('email',)

    def get_photo(self, obj):
        if obj.photo:
            thumbnail_options = {'crop': True, 'size': (75, 75)}
            thumbnailer = get_thumbnailer(obj.photo)
            return thumbnailer.get_thumbnail(thumbnail_options).url
        else:
            return None


class CreateReportSerializer(serializers.ModelSerializer):
    """
    used when POSTing a report
    """
    class Meta:
        model = Report