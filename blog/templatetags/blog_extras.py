"""
Custom template tags for showing content on the right-side navi menu
- recent blog posts
- archives
- tags
- categories
"""
from django import template
from blog import models

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_blog_posts(context, num=5):
    # implement template tag for showing the latest blog posts with specific number
    return {
        'recent_post_list': models.BlogPost.objects.all()[:num],
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    # implement template tag for showing the archived blog posts
    return {
        'datetime_list': models.BlogPost.objects.dates('created_at', 'month', order='DESC')
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    # implement template tag for showing all categories
    return {
        'category_list': models.Category.objects.all()
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    # implement template tag for showing all tags
    return {
        'tag_list': models.Tag.objects.all()
    }