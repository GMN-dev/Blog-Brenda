from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status = "published")


class Category(models.Model):
    categoryTitle = models.CharField(max_length=250, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")

    def __str__(self):
        return self.categoryTitle

class Post(models.Model):
    STATUS_CHOICE = (("draft", "Draft")
    ,("published", "Published"))
    title = models.CharField(max_length=250 , verbose_name="Título")
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Blog_Post")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices = STATUS_CHOICE, default="draft")
    
    categ = models.ManyToManyField(Category, verbose_name="Categoria do post:")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ("-publish",)

    postManager = PublishedManager()
    