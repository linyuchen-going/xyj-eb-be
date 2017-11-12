from django.db import models
from django.utils import timezone

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=16, null=True, blank=True)
    url = models.URLField()
    create_time = models.DateTimeField(default=timezone.now)
