# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents')
    date_created = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return self.docfile.name
    def get_pretty_date(self):
        return self.date_created.strftime('%h %d, %Y')