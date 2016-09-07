# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import CreateView

from rest_framework import filters
from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework.renderers import JSONRenderer
from rest_framework.settings import api_settings

from .serializers import ReportSerializer, CreateReportSerializer
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
    queryset = Report.objects.active()
    serializer_class = ReportSerializer

    distance_filter_field = 'points'
    filter_backends = (DistanceToPointFilter, filters.DjangoFilterBackend,)
    bbox_filter_include_overlapping = True  # Optional

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateReportSerializer
        else:
            return ReportSerializer


class MyReports(viewsets.ReadOnlyModelViewSet):
    queryset = Report.objects.active()
    serializer_class = ReportSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    def filter_queryset(self, queryset, *args, **kwargs):
        return queryset.filter(email=self.kwargs.get('email'))



class DeletedReportViewSet(ReportViewSet):
    queryset = Report.objects.deleted()