from django.shortcuts import render, HttpResponse
from blog.models import BlogPost


def base(request):
    """
    For rendering the base.html, includes the header, footer and right-side nav.
    - Header includes Website title, Nav links
    - Footer includes Copyright and other information
    - Right-side nav includes
    """
    context = {
        'website_title': 'White & Black',
    }

    return render(request, 'blog/base.html', context)


def index(request):
    """
    This function fetch all blog posts and render the index.html which is the main region of base.html
    """
    blog_posts = BlogPost.objects.all()

    context = {
        'website_title': 'White & Black',
        'blog_posts': blog_posts,
    }

    return render(request, 'blog/index.html', context)
