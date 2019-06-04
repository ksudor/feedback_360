from django.shortcuts import render
from .models import AskModel
from .forms import AskForm

def ask(request):
    form = AskForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AskForm()
        
    context = {
        'form': form
    }
    return render(request, 'askfeedback/ask.html', context)
