from django.db import models

# Create your models here.
class Vip(models.Model):
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username
        #return self.password
    
class Article(models.Model):
    title = models.CharField(u'标题',max_length=100,unique=True)
    autho = models.CharField(u'作者',max_length=100)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    category = models.CharField(u'分类',max_length=100)
    posted = models.DateField(db_index=True, auto_now_add=True)
    lastchange = models.DateTimeField(u'更新时间',auto_now=True, null=True)

    def __str__(self):
        return '%s' % self.title

class Article_detail(models.Model):
    pid = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    comment = models.TextField()
    lastchange = models.DateTimeField(u'更新时间',auto_now=True, null=True)

    def __str__(self):
        return self.comment
