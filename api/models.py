from django.db import models

# Create your models here.


class EShopHub(models.Model):
    name = models.CharField(max_length=100, default='Сыдр')
    description = models.TextField(blank=True)
    price = models.FloatField(default=10)
    data_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    exist = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='image/%Y/%m/$d',null=True)