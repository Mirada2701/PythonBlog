from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    image_url = models.ImageField(upload_to='images/', null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title