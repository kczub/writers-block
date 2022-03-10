import datetime
from django.db import models
from django.utils.text import slugify
from django.contrib import admin
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from tinymce.models import HTMLField

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    # snippet = models.CharField(max_length=255)
    content = HTMLField()
    slug = models.SlugField(blank=True, null=True)
    published = models.BooleanField('publish', default=False, blank=False, null=False)
    pub_date = models.DateTimeField('date published', blank=True, null=True)
    # updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        elif self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        
        if self.published is True:
            self.pub_date = timezone.now()
        else:
            self.pub_date = None
        super().save(*args, **kwargs)

    # @admin.display(
    #     boolean=True,
    #     ordering='pub_date',
    #     description='Published recently?',
    # )
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name}"
