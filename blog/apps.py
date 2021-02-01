from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = '博客管理'  # setup a verbose name on admin site for blog app
