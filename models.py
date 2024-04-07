from django.db import models

class Information(models.Model):
    name = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()
    description = models.TextField(blank=True)
