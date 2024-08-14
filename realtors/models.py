from django.db import models

# Create your models here.
class Realtor(models.Model):
    name = models.CharField()
    photo: models.CharField()
    description: models.TextField()
    email: models.EmailField()
    phone: models.CharField()
    is_mvp: models.BooleanField(0)
    hire_date: models.DateField()