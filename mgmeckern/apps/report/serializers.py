# -*- coding: utf-8 -*-
from django.conf import settings
from rest_framework import serializers

from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    """
    used when GETing a report hides email and adds a few 
    interesting fields
    """
    photo = serializers.SerializerMethodField('get_photo_url')
    thumbnail = serializers.SerializerMethodField('get_thumbnail_url')
    css_severity = serializers.CharField(source='css_severity', read_only=True, required=False)
    display_severity = serializers.CharField(source='display_severity', read_only=True, required=False)

    class Meta:
        model = Report
        exclude = ('email',)

    def get_photo_url(self, obj):
        try:
            return obj.photo.url
        except Exception as e:
            return None

    def get_thumbnail_url(self, obj):
        try:
            return obj.thumbnail.url
        except Exception as e:
            return obj.thumbnail



class CreateReportSerializer(serializers.ModelSerializer):
    """
    used when POSTing a report
    """
    class Meta:
        model = Report