from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse('This is Home page')


def about(request):
    return HttpResponse('This is about page')
