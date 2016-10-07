from django.db import models

class Manufacturer(models.Model):
    company_name = models.CharField(max_length=30)


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=20)