from django.db import models
from .category import Category
from django.contrib.auth.models import User


class Product(models.Model):
    """Models for products of OFF database"""
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField()
    API_link = models.URLField()
    photo = models.URLField()
    nutriscore = models.CharField(max_length=1)
    nutrient_100g = models.TextField(null=True)
    categories = models.ManyToManyField(Category)
    favorites = models.ManyToManyField(User, related_name="Favorite")

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'website'