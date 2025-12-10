from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    enrollment_date = models.DateField()
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name