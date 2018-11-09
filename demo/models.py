from django.db import models

# Create your models here.
class Vip(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username
        #return self.password
    
class Myblog(models.Model):
    title = models.CharField(max_length=100,unique=True)
    autho = models.CharField(max_length=100,unique=True)
    slug = models.CharField(max_length=100,unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)

    def __str__(self):
        return '%s' % self.title