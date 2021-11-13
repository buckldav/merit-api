from django.db import models
from organizations.models import BlogAPIKey


class Post(models.Model):
    url = models.URLField(help_text="URL of the post associated with the comments")


class Comment(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, default="Anonymous")
    content = models.TextField()

    blog_api_key = models.ForeignKey(to=BlogAPIKey, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
