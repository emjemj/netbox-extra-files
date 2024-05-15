from django import forms

from .models import ExtraFile

class ExtraFileUploadForm(forms.ModelForm):
    class Meta:
        model = ExtraFile
        fields = [ 'name', 'file', 'circuit' ]


