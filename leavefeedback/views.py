from django.shortcuts import render
from .models import LeaveModel
from .forms import LeaveForm

def leave(request):
    context = {"form": LeaveForm}
    return render(request, 'leavefeedback/leave.html', context)
