# -*- coding: utf-8 -*-
from django.conf import settings
from rest_framework import serializers

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
        return '%s%s' % (settings.MEDIA_URL, obj.photo)


class CreateReportSerializer(serializers.ModelSerializer):
    """
    used when POSTing a report
    """
    class Meta:
        model = Report