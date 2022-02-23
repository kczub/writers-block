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
    content = HTMLField()
    # content = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # print("Model save method called")
        if self.slug is None:
            # print(f"Slug is None - {self.slug is None}")
            self.slug = slugify(self.title)
            # print("Slugified title, set slug")

        elif self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        # print("Done model save slug checks")
        super().save(*args, **kwargs)
        # print("Model SAVED")

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

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
