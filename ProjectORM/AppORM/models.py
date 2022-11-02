from django.db import models

# Create your models here.
# Create model Post , it should have the following attributes :
# Title : char field
# Content : text field
# is_published : boolean field
# publish_date : datetime field

class Post(models.Model):
    Title = models.CharField(max_length=514)
    Content = models.TextField()
    is_published = models.BooleanField(default=False)
    publish_date = models.DateField()