from django.db import models


class School(models.Model):
    address = models.CharField(max_length=30)
    school_name = models.CharField(max_length=30)


class PhoneNumber(models.Model):
    first_number = models.CharField(max_length=3)
    middle_number = models.CharField(max_length=4)
    last_number = models.CharField(max_length=4)

class Marry(models.Model):
    marry = models.BooleanField(default=False)

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    marry = models.ForeignKey(Marry, on_delete=models.CASCADE, null=True)

class Coffee(models.Model):
    num = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=10)