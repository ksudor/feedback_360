from django import forms
from django.forms import Textarea
from .models import AskModel
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from datetime import date

class AskForm(forms.ModelForm):
    class Meta:
        model = AskModel
        fields = [
            'email',
            'emails',
            'deadline'
        ]
        widgets = {
            'emails': Textarea(attrs={'class': "form-control", 'rows': 10, 'id': "emails"}),
        }

    # def clean(self):
    #     data = self.cleaned_data
    #     deadline_data = data['deadline']
    #     emails_list = data['emails']
    #     emails_list = emails_list.replace(',', ' ').split()
    #     for email in emails_list:
    #         validate_email(email)
    #     my_set = set(emails_list)
    #
    #     if len(emails_list)<2:
    #         raise forms.ValidationError("Please, enter more than one email address!")
    #
    #     if len(my_set)!=len(emails_list):
    #         raise forms.ValidationError("Please, enter unique email addresses!")
    #
    #     if deadline_data < date.today():
    #         raise forms.ValidationError("The deadline date can't be in the past!")
    #     return data
    def clean_email(self):
        email_field = self.cleaned_data['email']
        return email_field
    
    def clean_emails(self):
        emails_list = self.cleaned_data['emails']
        emails_list = emails_list.replace(',', ' ').split()
        for email in emails_list:
            validate_email(email)

        if len(emails_list)<2:
            raise forms.ValidationError("Please, enter more than one email address!")

        my_set = set(emails_list)
        if len(my_set)!=len(emails_list):
            raise forms.ValidationError("Please, enter unique email addresses!")
        return emails_list

    def clean_deadline(self):
        deadline_data = self.cleaned_data['deadline']
        if deadline_data < date.today():
            raise forms.ValidationError("The deadline date can't be in the past!")
        return deadline_data

    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'class': "form-control", 'id': "email"})
        self.fields['deadline'].widget = forms.SelectDateWidget(attrs={'id': "date"})
