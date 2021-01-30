from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Tag(models.Model):
    """
    Model for tags
    """
    tag_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return 'tag name:'


class Category(models.Model):
    """ Model for categories """
    category_name = models.CharField(max_length=32)


class Comment(models.Model):
    """ Model for comments """

    comment_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # user =
    #
    # To create a recursive relationship – an object that has a many-to-one relationship with itself
    parent_id = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True, blank=True)


class BlogPost(models.Model):
    """ Model for a blog post """

    # basic fields
    title = models.CharField(max_length=64)
    text = models.TextField()
    excerpt = models.CharField(max_length=128)
    views = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # relational fields
    # ONE user can post MANY blog posts and ONE specific blog post belongs to ONE user
    author = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default='Admin')

    # ONE blog post can have MANY tags and ONE tag can filter MANY blog posts
    tags = models.ManyToManyField(to=Tag, blank=True)

    # ONE blog post belongs to ONE category and ONE category contains MANY blog posts
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True, blank=True)

    # ONE blog posts contains MANY comments and ONE comment only belongs to ONE specific blog post
    comments = models.ForeignKey(to=Comment, on_delete=models.SET_NULL, null=True, blank=True)

