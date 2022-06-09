from email.policy import default
from django.db import models


class Kategori(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.name


class Kelime(models.Model):
    name = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(
        Kategori, null=True, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="kelimeler/%Y/%m/%d/", default="kelimeler/default.jpg")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
