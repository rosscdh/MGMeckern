# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .serializers import CreateReportSerializer, ReportSerializer

from .models import Report


class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get_serializer_class(self):
         if self.request.method == 'POST':
            return CreateReportSerializer
         else:
            return ReportSerializer