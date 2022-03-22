from django.db import models

class Comment (models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    rider = models.ForeignKey("Rider", on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField()