from django.db import models

# Create your models here.
class notes(models.Model):
    product =models.CharField(max_length=50)
    detail =models.TextField()
