from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost, Category, Tag
from django.utils.text import slugify
import markdown2


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


def blog_post_detail(request, blog_post_id):
    """
    get the content of a specific blog post
    """
    # to fetch the blog post
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)

    # convert markdown into html tags with code friendly css style
    md2html = markdown2.markdown(
        blog_post.text,
        extras=[
            'fenced-code-blocks',
            'code-color',
            'code-friendly',
            'toc'
        ],
    )
    blog_post.text = md2html # html tags
    blog_post.toc = md2html.toc_html # table of content

    context = {
        'website_title': 'White & Black',
        'blog_post': blog_post,
    }

    return render(request, 'blog/blog_post_detail.html', context)


def archive(request, year, month):
    """
    according to the year and month to show blog posts
    """
    # to fetch blog posts with specific year and month
    blog_posts = BlogPost.objects.filter(created_at__year=year, created_at__month=month)

    context = {
        'website_title': 'White & Black',
        'blog_posts': blog_posts,
    }

    return render(request, 'blog/index.html', context)


def category(request, cate_id):
    """
    to show all blog posts with specific category id
    """
    # to fetch the category id and to filter the blog posts with this id
    cate = get_object_or_404(Category, pk=cate_id)
    blog_posts = BlogPost.objects.filter(category=cate)

    context = {
        'website_title': 'White & Black',
        'blog_posts': blog_posts,
    }

    return render(request, 'blog/index.html', context)


def tags(request, tag_id):
    """
    to show all blog posts with specific tag id
    """
    # to search the tag with the specific tag id and return all the blog posts with this tag
    tag = get_object_or_404(Tag, pk=tag_id)
    blog_posts = BlogPost.objects.filter(tags=tag)

    context = {
        'website_title': 'White & Black',
        'blog_posts': blog_posts,
    }

    return render(request, 'blog/index.html', context)