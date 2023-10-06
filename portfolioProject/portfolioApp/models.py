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


class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    description=models.TextField(max_length=200)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    skill=models.CharField(max_length=150)
    experience=models.IntegerField()

    def __str__(self):
        return self.skill
    
    