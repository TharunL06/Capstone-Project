from django.db import models

# Create your models here.
# creating the blog table

class Blog(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    authorName=models.CharField(max_length=200)
    image=models.ImageField(upload_to='blog',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
