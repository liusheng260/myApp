from django.db import models

# Create your models here.
class Vip(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username
        return self.password
    
