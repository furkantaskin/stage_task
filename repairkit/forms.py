from django import forms
from .models import Operation


class EditForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['description', 'operation_date', 'car']