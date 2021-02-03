from django.shortcuts import render, get_object_or_404, redirect
from blog import models
from comment import forms
from django.views.decorators.http import require_POST


@require_POST
def submit_comment(request, blog_post_id):

    blog_post = get_object_or_404(models.BlogPost, pk=blog_post_id)

    form = forms.CommentForm(request.POST)

    if form.is_valid():

        new_comment = form.save(commit=False)
        new_comment.blog_post = blog_post
        new_comment.save()

        return redirect(blog_post)

    context = {
        'blog_post': blog_post,
        'form': form,
    }

    return render(request, 'comments/preview.html', context)