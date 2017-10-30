from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    subject = models.CharField(max_length=50, blank=False, null=False)
    body = models.CharField(max_length=250, blank=False, null=False)
    user = models.ForeignKey(User)
