from django.urls import path
from comment import views

app_name = 'comment'

urlpatterns = [
    path('comments/<int:blog_post_id>', views.submit_comment, name='submit_comment'), # comment's detail
]