from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'blog/base.html', {'website_title': 'White & Black'})
