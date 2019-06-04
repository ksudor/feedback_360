from django import forms
from .models import AskModel
from django.forms import Textarea
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from datetime import date
from django.core.mail import send_mail


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

    def clean_deadline(self):
        deadline_date = self.cleaned_data['deadline']
        if deadline_date < date.today():
            raise forms.ValidationError("The deadline date can't be in the past!")
        return deadline_date

    def init(self, *args, **kwargs):
        super(AskForm, self).init(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'class': "form-control", 'id': "email"})
        self.fields['deadline'].widget = forms.DateField(attrs={'id': "date"},validators=[present_or_future_date])
        
        """Check if value consists only of valid emails."""
        emails_list = self.fields['emails']
        emails_list = emails_list.replace(',', ' ').split()
        for email in emails_list:
            validate_email(email)

        """Check if emails are more than one."""
        if len(emails_list)<2:
            raise forms.ValidationError("Please, enter more than one email address!")

        """Save only unique emails."""
        my_set = set(emails_list)
        

        if len(my_set)!=len(emails_list):
            raise forms.ValidationError("Please, enter unique email addresses!")
        
        send_mail(
        'Leave Feedback',
        'Please provide your feedback for' + self.fields['email'] + "\nDeadline Date:" + self.fields['deadline'] + "\nLeave Feedback Page: http://feedback360.998899.xyz:8888/leavefeedback_v1/",
        'feedback_360@ukr.net',
        [emails_list],
        fail_silently=False,
        )