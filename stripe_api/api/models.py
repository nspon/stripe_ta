from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=119)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name