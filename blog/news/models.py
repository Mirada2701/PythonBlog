from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    image_url = models.URLField(null=True, blank=True)

