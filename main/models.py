from django.db import models

# Create your models here.
class userDetails(models.Model):
    user_id         = models.IntegerField(unique=True)
    user_name       = models.CharField(max_length=100)
    user_address    = models.CharField(max_length=200)
    user_email      = models.EmailField(max_length=100)
    user_phone      = models.CharField(max_length=20)

