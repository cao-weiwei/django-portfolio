"""
Custom template tags for showing comments on the blog post page
- comment form
- comment list
"""
from django import template
from comment import forms, models

register = template.Library()


@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, blog_post, form=None):
    # implement template tag for showing the comment form
    if not form:
        form = forms.CommentForm()

    return {
        'form': form,
        'blog_post': blog_post
    }


@register.inclusion_tag('comments/inclusions/_comment_list.html', takes_context=True)
def comment_list(context, blog_post_id):
    # implement template tag for showing the list of comments
    comment_list = models.Comment.objects.filter(blog_post_id=blog_post_id)
    total_cnt_comment = comment_list.count()

    return {
        'comment_list': comment_list,
        'total_cnt_comment': total_cnt_comment,
    }