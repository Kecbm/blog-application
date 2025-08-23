from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Order the posts by the inverse publish date
    # The '-' sign means inverse
    # The first post will be the most recent
    class Meta:
        ordering = ['-publish']

    # Return the title of the blog post as a string
    def __str__(self):
        return self.title