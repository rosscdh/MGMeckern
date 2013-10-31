# -*- coding: utf-8 -*-
from django.db import models
from . import SEVERITY_CHOICES


class Report(models.Model):
    """
    User report model used to store the actual report
    """
    email = models.EmailField()
    comment = models.TextField()
    address = models.CharField(max_length=255, blank=True)
    severity = models.IntegerField()
    lat = models.DecimalField(max_digits=22, decimal_places=19)
    lon = models.DecimalField(max_digits=22, decimal_places=19)

    date_created = models.DateTimeField(auto_now=False, auto_now_add=True, db_index=True)
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=True, db_index=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ['-id']

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