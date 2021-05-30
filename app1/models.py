from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=40)
    original_price=models.IntegerField()
    discounted_price=models.IntegerField()
    category=models.CharField(max_length=50)
    description=models.TextField()
    image=models.CharField(max_length=200)

class Customer(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    city = models.CharField(max_length=40)
    address = models.TextField()
    email = models.EmailField()
    Password = models.CharField(max_length = 12)

    class Meta:
        db_table = 'customer' 
      
    #to display object in string format
    def __str__(self):
        return self.name