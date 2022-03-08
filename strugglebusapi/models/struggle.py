from django.db import models

class Struggle(models.Model):
    label = models.CharField(max_length=50)