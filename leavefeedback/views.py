from django.shortcuts import render
from .models import LeaveModel
from .forms import LeaveForm

def leave(request):
    form = LeaveForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LeaveForm()

    context = {
        'form': form
    }
    return render(request, 'leavefeedback/leave.html', context)
