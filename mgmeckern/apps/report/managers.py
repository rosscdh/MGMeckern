# -*- coding: UTF-8 -*-
from django.db import models


class ReportManager(models.Manager):
    def active(self, **kwargs):
        return self.filter(is_deleted=False).filter(**kwargs)

    def deleted(self, **kwargs):
        return self.filter(is_deleted=True).filter(**kwargs)