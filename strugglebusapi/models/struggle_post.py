from django.db import models

class StrugglePost(models.Model):
    rider = models.ForeignKey("Rider", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)