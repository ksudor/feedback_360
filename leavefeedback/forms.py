from django import forms
from django.forms import Textarea
from .models import LeaveModel
from django.core.exceptions import ValidationError

class LeaveForm(forms.ModelForm):
    class Meta:
        model = LeaveModel
        fields = [
            'email',
            'good',
            'improve'
        ]
        widgets = {
            'good': Textarea(attrs={'class': "form-control", 'rows': 10, 'id': "good"}),
            'improve': Textarea(attrs={'class': "form-control", 'rows': 10, 'id': "improve"}),
        }

    def clean_good(self):
        good_data = self.cleaned_data['good']
        if len(good_data) < 100:
            raise forms.ValidationError("Sorry, too short feedback in What was good field!")
        return good_data

    def clean_improve(self):
        improve_data = self.cleaned_data['improve']
        if len(improve_data) < 100:
            raise forms.ValidationError("Sorry, too short feedback in Things to improve field!")
        return improve_data

    def __init__(self, *args, **kwargs):
        super(LeaveForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'class': "form-control", 'id': "email"})
