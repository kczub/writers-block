from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'author', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['author', 'title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'post', 'pub_date']
    search_fields = ['name']
