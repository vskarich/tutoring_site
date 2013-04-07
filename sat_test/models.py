from django.db import models
from accounts.models import UserProfile

class Test(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    location = models.CharField(max_length=50)
    is_practice_test = models.BooleanField(default=False)
    

class Score(models.Model):
    student = models.ForeignKey(UserProfile)
    test = models.ForeignKey(Test)
    math_score = models.IntegerField()
    verbal_score = models.IntegerField()
    analytic_score = models.IntegerField()
