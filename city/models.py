from django.db import models

# Create your models here.
class City(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length = 255)