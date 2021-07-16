from django.db import models

class Officer(models.Model):
    lastName = models.CharField(max_length=20, blank=False)
    firstName = models.CharField(max_length=20, blank=False)
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    bio = models.TextField(max_length=500, blank=True)
