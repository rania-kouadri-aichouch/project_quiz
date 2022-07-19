from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200,null=False)
    op1 = models.CharField(max_length=200,null=True,blank=False)
    op2 = models.CharField(max_length=200,null=True,blank=False)
    op3 = models.CharField(max_length=200,null=True,blank=False)
    answer = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question


class Result(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='user'
    )
    score = models.IntegerField(blank=False,null=True)
    correct = models.IntegerField(blank=False,null=True)
    wrong = models.IntegerField(blank=False,null=True)
    total = models.IntegerField(blank=False,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username
