from django.db import models
from django.contrib.auth.models import User

class Test(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    location = models.CharField(max_length=50)
    is_practice_test = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name + '  ' + self.date.strftime('%h %d, %Y')
    def get_pretty_date(self):
        return self.date.strftime('%h %d, %Y')


class Score(models.Model):
    student = models.ForeignKey(User)
    test = models.ForeignKey(Test)
    math_score = models.IntegerField()
    verbal_score = models.IntegerField()
    analytic_score = models.IntegerField()

    def __unicode__(self):
        return self.test.__unicode__() + '  ' + self.student.last_name + ', ' + self.student.first_name
