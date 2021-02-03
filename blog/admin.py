from django.contrib import admin
from blog.models import BlogPost, Tag, Category


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'category', 'all_tags')
    fields = ('title', 'text', 'excerpt', 'tags', 'category')

    def all_tags(self, obj):
        """
        return all the tags for current BlogPost instance
        """
        return ', '.join([tag.tag_name for tag in obj.tags.all()])

    def save_model(self, request, obj, form, change):
        """
        auto save current logged in user as the author
        """
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
