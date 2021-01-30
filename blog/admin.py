from django.contrib import admin
from blog.models import BlogPost, Tag, Category, Comment

admin.site.register(BlogPost)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
