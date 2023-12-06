from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100)
        
class Webpages(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    
class AccessRecode(models.Model):
    name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    data=models.DateField()
    author=models.CharField(max_length=100)