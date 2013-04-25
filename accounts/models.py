from django.db import models
from django.contrib.auth.models import User
from uploads.models import Document
from notes.models import Note

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    documents = models.ManyToManyField(Document, blank=True, null=True)
    #notes = models.ManyToManyField(Note, blank=True, null=True)