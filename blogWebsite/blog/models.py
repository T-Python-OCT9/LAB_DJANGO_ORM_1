from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    publish_date = models.DateField()
    is_published = models.BooleanField()

  

