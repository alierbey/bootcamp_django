from django.db import models

class Kelime(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    date =models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)


