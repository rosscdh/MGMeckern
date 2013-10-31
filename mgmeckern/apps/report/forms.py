# -*- coding: UTF-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from parsley.decorators import parsleyfy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from .models import Report


@parsleyfy
class ReportForm(forms.ModelForm):
    """
    Public Form for the report model
    """
    # lat = forms.CharField(widget=forms.HiddenInput)
    # lon = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Report
        exclude = ('is_deleted')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        #self.helper.layout = Layout()
        super(ReportForm, self).__init__(*args, **kwargs)


@parsleyfy
class AddressSearchForm(forms.Form):
    q = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input-lg col-lg-12', 'placeholder': 'Street Address...'}))

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        #self.helper.form_id = 'address-search-form'
        self.helper.layout = Layout(
            Fieldset(
                'Where is the problem?',
                'q',
            ),
        )
        super(AddressSearchForm, self).__init__(*args, **kwargs)