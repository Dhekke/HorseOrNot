from django.db import models


class Horse(models.Model):
    name = models.CharField(max_length=50)
    real_profile = models.CharField(max_length=30)
    horse_profile = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# Create your models here.
