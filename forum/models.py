from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.




class Question(models.Model):

    class Status(models.TextChoices):
        Draft = 'DF' ,'Draft'
        Puplished = 'PB' ,' Puplished'
        
    Author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    question = models.CharField(max_length=200)
    tags = TaggableManager()
    created_at = models.DateField(default=timezone.now)
    Content = models.TextField(max_length=20000)
    status = models.CharField(max_length=5,choices=Status.choices,default=Status.Draft)



    def __str__(self):
        return self.question
    

class Answers(models.Model):
    Author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Answer = models.CharField(max_length=1000)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="Answers_Question")
    created_at = models.DateField(default=timezone.now)
    
    

    def __str__(self):
        return self.Answer
