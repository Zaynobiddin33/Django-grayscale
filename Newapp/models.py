from django.db import models


# Create your models here.

class Notify(models.Model):
    email = models.CharField(max_length = 255)

    def __str__(self) -> str:
        return self.email