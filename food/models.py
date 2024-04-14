from django.db import models


# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_img = models.CharField(max_length=500, default="https://i.pinimg.com/736x/94/ee/2f/94ee2fda4931c26b3c55ed23d28e885e.jpg")

