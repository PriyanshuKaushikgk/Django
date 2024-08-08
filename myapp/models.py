from django.db import models

# Create your models here.

CATEGORY_CHOICE = [
    ("mens","mens"),
    ("women","women"),
    ("kids","kids"),
    ("electronic","electronic"),
    ("special_product","special_product")
]




class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    size = models.CharField(max_length=10)
    category = models.CharField(choices=CATEGORY_CHOICE,max_length=50)
    is_available = models.BooleanField(

    )


