from __future__ import unicode_literals
from django.db import models

# Create your models here.
class IMG(models.Model):
    captime = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='upload')