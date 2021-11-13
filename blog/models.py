from django.db import models
from organizations.models import BlogAPIKey


class Post(models.Model):
    url = models.URLField(help_text="URL of the post associated with the comments")


class CommentManager(models.Manager):
    def can_add(self, blog_api_key):
        limit = 50
        return self.model.objects.filter(blog_api_key=blog_api_key).count() < limit

    def create(self, **obj_data):
        if "blog_api_key" in obj_data and self.can_add(obj_data["blog_api_key"]):
            return super().create(**obj_data)
        else:
            return None  # Reached limit for key


class Comment(models.Model):
    objects = CommentManager()

    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, default="Anonymous")
    content = models.TextField()

    blog_api_key = models.ForeignKey(to=BlogAPIKey, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
