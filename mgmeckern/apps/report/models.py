# -*- coding: utf-8 -*-
from django.db import models


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