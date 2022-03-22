from django.db import models

class StrugglePost(models.Model):
    struggle = models.ForeignKey("Struggle", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)