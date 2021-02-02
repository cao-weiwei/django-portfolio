from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'), # homepage
    path('post/<int:post_id>', views.blog_post_detail, name='blog_post_detail'), # blog post detail page
    path('archives/<int:year>/<int:month>', views.archive, name='archive'), # archived blog posts
    path('categories/<int:cate_id>', views.category, name='category'), # category's blog posts
    path('tags/<int:tag_id>', views.tags, name='tag'), # tag's blog posts
]