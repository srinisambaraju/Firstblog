from django.shortcuts import render_to_response
from django.shortcuts import render

import aftership


# Create your views here.


def index(request):
    # return HttpResponse("<h1> This is an index page</h1>")
    # p = Posts.objects.all()[:10]
    # content = {
    #    'title': 'My First Post',
    #    'author': 'Srini',
    #    'date': '26th Sept 2018',
    #    'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ' \
    #            'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit' \
    #            ' in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui ' \
    #            'officia deserunt mollit anim id est laborum '
    # }


    api = aftership.APIv4('33ab0b24-106a-40e3-8220-4e5945d57c5e')
    couriers = api.couriers.all.get()
    slug = 'ups'
    number = '1Z6962EX0237415624'
    api.trackings.get(slug, number, fields=['title', 'created_at'])
    return render_to_response('aftershiptracking/index.html')


def about(request):
    return render(request, 'aftershiptracking/about.html')
