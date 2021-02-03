from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import markdown2


class Tag(models.Model):
    """
    Model for tags
    """
    tag_name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签列表'

    def __str__(self):
        return '%s' % self.tag_name


class Category(models.Model):
    """
    Model for categories
    """
    category_name = models.CharField(max_length=32)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类列表'

    def __str__(self):
        return '%s' % self.category_name


class BlogPost(models.Model):
    """
    Model for a blog post
    """
    # basic fields
    title = models.CharField(max_length=64)
    text = models.TextField()
    excerpt = models.CharField(max_length=128, null=True, blank=True, default='')
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # relational fields
    # ONE user can post MANY blog posts and ONE specific blog post belongs to ONE user
    author = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default='Admin')

    # ONE blog post can have MANY tags and ONE tag can filter MANY blog posts
    tags = models.ManyToManyField(to=Tag, blank=True)

    # ONE blog post belongs to ONE category and ONE category contains MANY blog posts
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章列表'
        ordering = ['-created_at']  # set the default ordering field

    def save(self, *args, **kwargs):
        """
        rewrite the save() method to set a default excerpt field
        """
        if self.excerpt is None:
            # if excerpt is empty, then an automatic excerpt will be generated
            # to covert markdown syntax into html tags
            md2html = markdown2.markdown(
                self.text,
                extras=[
                    'fenced-code-blocks',
                    'code-color',
                    'code-friendly',
                ],
            )
            # remove html tags and
            # fetch the first 64 characters from the main text
            self.excerpt = strip_tags(md2html)[:64]

        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        """
        get blog post's url
        """
        return reverse('blog:blog_post_detail', kwargs={'blog_post_id': self.id})

