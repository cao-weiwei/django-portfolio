from django.contrib import admin
from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'text', 'created_at', 'blog_post')
    fields = ['username', 'email', 'url', 'text', 'blog_post']


admin.site.register(Comment, CommentAdmin)