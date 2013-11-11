# -*- coding: UTF-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from parsley.decorators import parsleyfy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, HTML, ButtonHolder, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from . import SEVERITY_CHOICES
from .models import Report


@parsleyfy
class ReportForm(forms.ModelForm):
    """
    Public Form for the report model
    """
    severity = forms.ChoiceField(choices=SEVERITY_CHOICES.get_choices(), initial=0, widget=forms.RadioSelect)
    lat = forms.CharField(widget=forms.HiddenInput)
    lon = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Report
        exclude = ('is_deleted',)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'frm-create-report'
        self.helper.form_class = 'parsley'
        self.helper.layout = Layout(
            'email',
            'comment',
            'address',
            'severity',
            'lat',
            'lon',
            Button('btn-send-report', 'Report', css_id='id_btn-send-report', css_class='btn-send-report btn btn-warning'),
        )
        super(ReportForm, self).__init__(*args, **kwargs)


@parsleyfy
class AddressSearchForm(forms.Form):
    q = forms.CharField(label='', initial='', required=True, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': _('Street Address...')}))

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'frm-address-search'
        self.helper.form_class = 'form-inline parsley'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.attrs = {'role': 'form', 'data-validate': 'parsley'}

        self.helper.layout = Layout(
            Div(
                'q',
                Button('btn-search-btn', 'Search', css_id='search-btn', css_class='btn btn-info input-lg'),
                #Field('q', css_class='form-control col-md-offset-6 input-lg'),
                css_class='row '
            ),
            Div(
                HTML('<div class="row"><p>&nbsp;</p></div>'),
                Button('btn-add-marker-btn', 'Add Report', css_id='add-marker-btn', css_class='btn btn-lg btn-success hide'),
                HTML('<div class="row"><p>&nbsp;</p></div>'),
                css_class='row'
            ),
        )
        super(AddressSearchForm, self).__init__(*args, **kwargs)