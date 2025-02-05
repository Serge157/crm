from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=1)  # кількість в наявності
    image = models.ImageField(upload_to='flowers/', default='flowers/default.jpg')

    def __str__(self):
        return self.name
    


class FlowerSet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    flowers = models.ManyToManyField(Flower, related_name='flower_sets')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    

