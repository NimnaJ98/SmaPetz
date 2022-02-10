from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    picture = models.ImageField(upload_to='images', blank = True)
    body = models.TextField()
    liked = models.ManyToManyField(User, default=None, blank=True)
    tags = models.CharField(max_length=100, blank=True)
    #author
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    #string representation
    def __str__(self):
        return str(self.pk)

    #to get the users who liked the post
    def get_liked(self):
        return self.liked.all()
    
    #get no of likes
    @property
    def like_count(self):
        return self.liked.all().count()

    #check whether a particular user liked or not
    def get_user_liked(self, user):
        pass

    