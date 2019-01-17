from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def raasi_details(request):
    # article = article.objects.get(slug=slug)
    # return render(request, 'articles/article_detail.html', {'article': article})
    return HttpResponse("Raasi Details of the person")
