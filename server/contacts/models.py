from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
    portrait = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)