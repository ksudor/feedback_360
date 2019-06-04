from django import forms
from .models import LeaveModel

class LeaveForm(forms.Form):
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}))
    good = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '10', 'id': 'good'}))
    improve = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '10', 'id': 'improve'}))
