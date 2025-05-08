from django.db import models

class News(models.Model):
            title = models.CharField(max_length=200)
            content = models.TextField()
            pub_date = models.DateTimeField(auto_now_add=True)
            author = models.CharField(max_length=100)
            image = models.ImageField(upload_to='news_images/', blank=True, null=True)\
            
            def __str__(self):
                return self.title
