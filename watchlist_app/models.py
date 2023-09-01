from rest_framework.authtoken.models import Token
from typing import Iterable
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import related
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.fields import MaxValueValidator, MinValueValidator



class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=50)
    website = models.URLField()
    
    def __str__(self):
        return self.name
    

class WatchList(models.Model):
    title = models.CharField(max_length=52)
    description = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchlist")
    avg_rating = models.FloatField(default=0,validators=[MaxValueValidator(10)])
    number_rating = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    description = models.CharField(max_length=200,null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE,related_name="reviews")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.watchlist.title + " - " + str(self.rating)
    


# hooks for when review is created

@receiver(post_save, sender=Review)
def update_watchlist_review_count(sender,instance,**kwargs):
    watchlist = instance.watchlist
    watchlist.number_rating += 1
    watchlist.avg_rating = (watchlist.avg_rating + instance.rating)/2
    watchlist.save()
    


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)