from django.shortcuts import render
from .models import AskModel
from .forms import AskForm
from django.core.mail import send_mail

def ask(request):
    form = AskForm(request.POST or None)
    if form.is_valid():
        form.save()
        emails_list = form.cleaned_data['emails']
        for email in emails_list:
        	send_mail(
        	'Leave Feedback','Please provide your feedback for ' + form.clean_email() + "\nDeadline Date: " + form.clean_deadline().strftime('%m/%d/%Y') + "\nLeave Feedback Page: http://feedback360.998899.xyz:8888/leavefeedback/",'feedback360@998899.xyz', [email], fail_silently=False,)
        form = AskForm()
    context = {
        'form': form
    }
    return render(request, 'askfeedback/ask.html', context)
