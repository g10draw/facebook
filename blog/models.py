from django.db import models

from auth_manager.models import CustomUser

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.TextField()
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    likes = models.ManyToManyField(CustomUser, related_name='my_liked_posts', 
        null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, related_name='my_comments', 
        on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', 
        on_delete=models.CASCADE)
    text = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='following', 
        on_delete=models.CASCADE)
    following = models.ForeignKey(CustomUser, related_name='followers', 
        on_delete=models.CASCADE)