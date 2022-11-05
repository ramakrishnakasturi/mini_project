from django.db import models

# Create your models here.
                #Step-21
choice1 = (
    ("Male", "Male"),
    ("Female", "Female"),
)

choice2 = (
    ("Handbags", "Handbags"),
    ("Footwear", "Footwear"),
    ("Jewelery", "Jewelery"),
    ("Tshirts", "Tshirts"),
    ("Watches", "Watches"),
    ("Shades", "Shades"),
)

class Item(models.Model):

    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    gender = models.CharField(max_length=30,choices = choice1)
    category = models.CharField(max_length=30,choices = choice2)
    price = models.IntegerField()
    discount = models.IntegerField()
    user = models.CharField(max_length=30)
                        #


