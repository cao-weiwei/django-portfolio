from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.blog_post_detail, name='blog_post_detail'),
]