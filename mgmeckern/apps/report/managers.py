# -*- coding: UTF-8 -*-
from django.db import models


class ReportManager(models.Manager):

    def active(self, **kwargs):
        return self.public(is_deleted=False)

    def private(self, **kwargs):
        return self.filter(is_public=False).filter(**kwargs)

    def public(self, **kwargs):
        return self.filter(is_public=True).filter(**kwargs)

    def deleted(self, **kwargs):
        return self.filter(is_deleted=True).filter(**kwargs)