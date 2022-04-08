from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.

class profile  (models.Model):
    bio = models.CharField(max_length=250)
    image = CloudinaryField('image/', default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.bio
    
    def save_projects(self):
        self.save()
    def delete_projects(self):
        self.delete()

class Projects (models.Model):
    title = models.CharField(max_length=60)
    image = CloudinaryField('image/', default="")
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    link = models.CharField(max_length=60)
    def __str__(self):
        return self.title
    
    def save_projects(self):
        self.save()
    def delete_projects(self):
        self.delete()