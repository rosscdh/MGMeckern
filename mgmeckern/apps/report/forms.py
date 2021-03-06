# -*- coding: UTF-8 -*-
from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


from parsley.decorators import parsleyfy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Button, Submit
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineRadios

from . import SEVERITY_CHOICES
from .models import Report


@parsleyfy
class AddressSearchForm(forms.Form):
    q = forms.CharField(label='', initial='', required=True, widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': _('Street Address...')}))

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'frm-address-search'
        self.helper.form_class = 'form-inline parsley'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.attrs = {'role': 'form', 'data-validate': 'parsley'}

        self.helper.layout = Layout(
            Div(
                'q',
                HTML('<span id="search-btn" class="glyphicon glyphicon-search search-btn btn btn-info"></span>'),
                HTML('<span id="add-marker-btn" class="glyphicon glyphicon-plus add-marker-btn btn btn-success hide"></span>'),
                HTML('<a class="nav-btn pull-right" href="%s"><span id="about-btn" class="glyphicon glyphicon-info-sign btn btn-default"></span></a>' % reverse('public:about')),
                css_class=''
            ),
        )
        super(AddressSearchForm, self).__init__(*args, **kwargs)


@parsleyfy
class ReportForm(forms.ModelForm):
    """
    Public Form for the report model
    """
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    lat = forms.CharField(widget=forms.HiddenInput)
    lon = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Report
        exclude = ('severity', 'is_deleted', 'is_public', 'photo_is_public', 'report_type')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'frm-create-report'
        self.helper.form_action = reverse('report:create')

        self.helper.form_class = 'form form-horizontal parsley'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
            PrependedText('email', '@'),
            'comment',
            'address',
            'photo',
            'lat',
            'lon',
            Submit('btn-send-report', 'Report', css_id='id_btn-send-report', css_class='btn-send-report btn btn-warning'),
        )
        super(ReportForm, self).__init__(*args, **kwargs)
