from django.db import models
class Pizza(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Topping(models.Model):
    name = models.CharField(max_length=100)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

# Create your models here.
