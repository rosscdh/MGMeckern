# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import CreateView

from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.renderers import JSONRenderer

from .serializers import CreateReportSerializer, ReportSerializer
from .models import Report
from .forms import ReportForm


class CreateReportView(CreateView):
    form_class = ReportForm
    template_name = 'report/report_form.html'

    def form_valid(self, form):
        form.save()
        json_response = ReportSerializer(form.instance)
        return HttpResponse(JSONRenderer().render(json_response.data), content_type='application/json')


class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    parser_classes = (FileUploadParser,)
    queryset = Report.objects.active()
    serializer_class = ReportSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateReportSerializer
        else:
            return ReportSerializer


class DeletedReportViewSet(ReportViewSet):
    queryset = Report.objects.deleted()