from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from blog import models
from comment import forms
from django.views.decorators.http import require_POST


@require_POST
def submit_comment(request, blog_post_id):
    """
    submit the comment form with a specific blog post
    """
    blog_post = get_object_or_404(models.BlogPost, pk=blog_post_id)

    form = forms.CommentForm(request.POST) # filled the form with POST data

    if form.is_valid():
        # the form data is legal and bind with the blog post
        new_comment = form.save(commit=False)
        new_comment.blog_post = blog_post
        new_comment.save()

        # successfully send a comment on current post
        messages.add_message(request, level=messages.SUCCESS, message='评论发表成功！', extra_tags='success')

        return redirect(blog_post)

    context = {
        'blog_post': blog_post,
        'form': form,
    }

    # failed to send a comment
    messages.add_message(request, level=messages.ERROR, message='评论发表失败！请修改表单中的错误后重新提交。', extra_tags='danger')

    return render(request, 'comments/preview.html', context)