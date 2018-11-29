from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here. Add different views.


def automation_home(request):
    return render(request, 'automation/automation_home.html')
