# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .serializers import CreateReportSerializer, ReportSerializer

from .models import Report


class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Report.objects.active()
    serializer_class = ReportSerializer

    def get_serializer_class(self):
         if self.request.method == 'POST':
            return CreateReportSerializer
         else:
            return ReportSerializer


class DeletedReportViewSet(ReportViewSet):
    queryset = Report.objects.deleted()