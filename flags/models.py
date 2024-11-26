
from django.db import models

class Flag(models.Model):
    image = models.ImageField(upload_to='flags/')
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

# Create your models here.
