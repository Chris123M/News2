from django.db import models
from django.db import models

class story(models.Model):
    heading = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

