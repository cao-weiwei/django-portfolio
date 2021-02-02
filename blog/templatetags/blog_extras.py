from django import template
from blog import models

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_blog_posts(context, num=5):
    # return the latest num blog posts
    return {
        'recent_post_list': models.BlogPost.objects.all().order_by('-created_at')[:num],
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):

    return {
        'datetime_list': models.BlogPost.objects.dates('created_at', 'month', order='DESC')
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):

    return {
        'category_list': models.Category.objects.all()
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):

    return {
        'tag_list': models.Tag.objects.all()
    }