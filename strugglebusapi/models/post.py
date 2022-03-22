from django.db import models

class Post (models.Model):
    rider = models.ForeignKey("Rider", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    bus = models.ForeignKey("Bus", on_delete=models.CASCADE)
    struggle = models.ManyToManyField("Struggle", through="StrugglePost")
    description = models.TextField()
    date = models.DateField()