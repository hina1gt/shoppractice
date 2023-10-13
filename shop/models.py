from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    def __str__(self):
        return f'{self.username}'
    
class Rubric(models.Model):

    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'
    
class Product(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='products-image')
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'