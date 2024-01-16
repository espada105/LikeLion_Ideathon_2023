from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    image1 = models.ImageField(upload_to = 'blog', blank=True, null=True)
    image2 = models.ImageField(upload_to = 'blog', blank=True, null=True)
    image3 = models.ImageField(upload_to = 'blog', blank=True, null=True)
    image4 = models.ImageField(upload_to = 'blog', blank=True, null=True)

    def __str__(self):
        return self.body
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
# class Photo(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#     image1 = models.ImageField(upload_to = 'blog', blank=True, null=True)
#     image2 = models.ImageField(upload_to = 'blog', blank=True, null=True)
#     image3 = models.ImageField(upload_to = 'blog', blank=True, null=True)
#     image4 = models.ImageField(upload_to = 'blog', blank=True, null=True)


# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#     content = models.TextField()