from django.db import models

# Create your models here.
class users(models.Model):
    userID = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=100)

class userData(models.Model):
    userId = models.IntegerField(primary_key=True)
    userHealth = models.IntegerField()  
    userAmmo = models.IntegerField()
    userHighscroe = models.IntegerField()
    userFirstTime = models.BooleanField(default=False)
