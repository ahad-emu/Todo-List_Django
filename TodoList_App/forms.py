from django import forms
from .models import List

class FormList(forms.ModelForm):
    name = forms.CharField()
    roll = forms.CharField()
    section = forms.CharField()
    
    class Meta:
        model = List
        fields = ['name', 'roll', 'section']
