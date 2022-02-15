from django.contrib import admin

from .models import Post

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']

admin.site.register(Post, BlogAdmin)
