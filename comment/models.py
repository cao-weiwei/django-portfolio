from django.db import models
from django.utils.timezone import now
from blog.models import BlogPost


class Comment(models.Model):

    username = models.CharField(max_length=64)
    email = models.EmailField()
    url = models.URLField(blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=now)

    # ONE blog posts contains MANY comments and ONE comment only belongs to ONE specific blog post
    blog_post = models.ForeignKey(to=BlogPost, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论列表'

    def __str__(self):
        return '{}: {}'.format(self.username, self.text[:10])
