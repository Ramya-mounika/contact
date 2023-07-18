from django.db import models

class ContactData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    email=models.EmailField(max_length=60)
    mobile=models.BigIntegerField()
    location=models.CharField(max_length=100)
