from django.db import models

from auth_manager.models import CustomUser

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.TextField()
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    likes = models.ManyToManyField(CustomUser, related_name='my_liked_posts')
    posted_at = models.DateTimeField(auto_now_add=True)