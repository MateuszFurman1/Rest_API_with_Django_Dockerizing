from datetime import timezone
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Post(models.Model):
    class PostObject(models.Manager):
        def get_qyeryset(self):
            return super().get_qyeryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique_for_date='published')
    published = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObject()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
