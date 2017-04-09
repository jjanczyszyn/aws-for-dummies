from django.db import models

# Create your models here.


class Image(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=128, default=None, null=True)
