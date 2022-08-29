from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username

class Journals(models.Model):
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    time_posted = models.TimeField(auto_now_add=True)


    def __str__(self) :
        return f"{self.posted_by}'s journal"
