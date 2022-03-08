from django.db import models

class Bus(models.Model):
    label = models.Charfield(max_length=50)