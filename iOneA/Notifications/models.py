from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200, default='notification')
    url = models.URLField(null='', blank='', default='')
    ifViewed = models.BooleanField(null=False, default=False)
    ifAccepted = models.BooleanField(null=False, default=False)
    def __str__(self):
        return self.message