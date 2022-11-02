from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length = 512)
    Content = models.TextField()
    is_published = models.BooleanField()
    publish_data = models.DateTimeField()
