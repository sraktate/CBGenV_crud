from django.db import models

# Create your models here.
class Laptop(models.Model):
     company_name= models.CharField(max_length=30)
     model_name = models.CharField(max_length=30)
     Ram = models.IntegerField()
     rom = models.IntegerField()
     processor = models.CharField(max_length=10)
     price = models.FloatField()