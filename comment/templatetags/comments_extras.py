from django import template
from comment import forms

register = template.Library()


@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, blog_post, form=None):
    if not form:
        form = forms.CommentForm()

    return {
        'form': form,
        'blog_post': blog_post
    }