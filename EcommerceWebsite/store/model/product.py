from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name