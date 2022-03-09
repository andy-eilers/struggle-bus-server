from django.db import models

class Bus(models.Model):
    label = models.CharField(max_length=50)