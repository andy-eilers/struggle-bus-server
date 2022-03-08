from django.db import models

class Post (models.Model):
    bus = models.ForeignKey("Bus", on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()