from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class BlogPosts(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    slug = models.SlugField(max_length=120, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, max_length=5000, verbose_name='Content')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Publication Update Time')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=120, db_index=True, verbose_name='Category Name')
    slug = models.SlugField(max_length=120, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id', 'name']


class Comment(models.Model):
    comment_message = models.TextField(max_length=3000, verbose_name='Comment')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')
    posts = models.ForeignKey(BlogPosts, null=True, on_delete=models.CASCADE, verbose_name='Comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')

    def __str__(self):
        return self.comment_message

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-time_create', 'id']