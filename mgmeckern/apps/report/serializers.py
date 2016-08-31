# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.humanize.templatetags.humanize import naturaltime

from rest_framework import serializers

from .models import Report

import markdown2
MD = markdown2.Markdown()


class ReportSerializer(serializers.ModelSerializer):
    """
    used when GETing a report hides email and adds a few 
    interesting fields
    """
    comment = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    date_modified = serializers.SerializerMethodField()
    css_severity = serializers.CharField(read_only=True, required=False)
    display_severity = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = Report
        exclude = ('email',)

    def get_comment(self, obj):
        return mark_safe(MD.convert(obj.comment))

    def get_date_created(self, obj):
        return naturaltime(obj.date_created)

    def get_date_modified(self, obj):
        return naturaltime(obj.date_modified)

    def get_photo(self, obj):
        try:
            return obj.photo.url
        except Exception as e:
            return None

    def get_thumbnail(self, obj):
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