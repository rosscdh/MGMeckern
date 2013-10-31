# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    css_severity = serializers.CharField(source='css_severity', read_only=True, required=False)
    display_severity = serializers.CharField(source='display_severity', read_only=True, required=False)

    class Meta:
        model = Report
        exclude = ('email',)