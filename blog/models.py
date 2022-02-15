import datetime
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.db import models

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self) -> str:
        return self.title