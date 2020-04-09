from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    Name = models.CharField(max_length=50, unique=True)


class WebPage(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    Url = models.URLField()


class AccessRecord(models.Model):
    WebPage = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    Date = models.DateField()


class UserInfo(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    DateOfBirth = models.DateField(blank=True)
    ProfilePicture = models.ImageField(upload_to='profile_pics',blank=True)
