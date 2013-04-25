from django.db import models


class Note(models.Model):
    """Model to save our note"""
    title   = models.CharField(max_length=255)
    content = models.TextField()
    #automatically add timestamps when object is created
    date_created = models.DateTimeField(auto_now_add=True)
    #automatically add timestamps when object is updated
    last_update = models.DateTimeField(auto_now=True) #
    def __unicode__(self):
        return self.title
    def get_pretty_date(self):
        return self.date_created.strftime('%h %d, %Y')

