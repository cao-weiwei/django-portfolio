from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):
    """
    Create a comment form
    """
    class Meta:
        model = Comment
        fields = ['username', 'email', 'url', 'text']