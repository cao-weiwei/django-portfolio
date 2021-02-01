from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost
import markdown2


# def base(request):
#     """
#     For rendering the base.html, includes the header, footer and right-side nav.
#     - Header includes Website title, Nav links
#     - Footer includes Copyright and other information
#     - Right-side nav includes
#     """
#     context = {
#         'website_title': 'White & Black',
#     }
#
#     return render(request, 'blog/base.html', context)


def index(request):
    """
    This function fetch all blog posts and render the index.html which is the main region of base.html
    """
    blog_posts = BlogPost.objects.all()

    context = {
        'website_title': 'White & Black',
        'blog_posts': blog_posts,
    }

    return render(request, 'blog/index.html', context)


def blog_post_detail(request, post_id):
    blog_post = get_object_or_404(BlogPost, pk=post_id)
    # blog_post.text = markdown.markdown(
    #     blog_post.text,
    #     extentions=[
    #         'markdown.extensions.extra',
    #         'markdown.extensions.codehilite',
    #         # 'markdown.extensions.fenced_code',
    #         'markdown.extensions.toc',
    #     ])
    blog_post.text = markdown2.markdown(
        blog_post.text,
        extras=[
            'fenced-code-blocks',
            'code-color',
            'code-friendly'
        ]
    )

    context = {
        'website_title': 'White & Black',
        'blog_post': blog_post,
    }

    return render(request, 'blog/blog_post_detail.html', context)
