from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
            title = models.CharField(max_length=200)
            content = models.TextField()
            pub_date = models.DateTimeField(auto_now_add=True)
            author = models.CharField(max_length=100)
            image = models.ImageField(upload_to='news_images/', blank=True, null=True)\
            
            def __str__(self):
                return self.title
            
class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
