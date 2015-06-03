from django.db import models

# Create your models here.
# extending the User model https://docs.djangoproject.com/en/1.6/topics/auth/customizing/

from django.contrib.auth.models import User

class GrumblrUser(models.Model):
    user = models.OneToOneField(User) #one to one correspondance with Django User model
    aboutme = models.CharField(max_length=50)
    followers = models.ManyToManyField('self', related_name='user_followers', symmetrical=False)
    # its not a symmetric relation
    following = models.ManyToManyField('self', related_name='following_users', symmetrical=False)
    blocked = models.ManyToManyField('self', related_name='blocked_users', symmetrical=False)
    #image = models.ImageField(name=None, blank=True)

class Grumbl(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=42)
    user = models.ForeignKey(User)
    #image = models.ImageField(name=None, blank=True)
    # a grumbl can have likes, dislikes and comments
    likes = models.ManyToManyField(GrumblrUser, related_name='likes')
    dislikes = models.ManyToManyField(GrumblrUser, related_name='dislikes')

class GrumblComment(models.Model):
	comment = models.CharField(max_length=50)
	#image = models.ImageField(name=None, blank=True)
	grumbl = models.ForeignKey(Grumbl)