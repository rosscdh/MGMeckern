# -*- coding: UTF-8 -*-
from django.contrib import admin

#from leaflet.admin import LeafletGeoAdmin
from .models import Report

#admin.site.register(Report, LeafletGeoAdmin)
admin.site.register([Report])
