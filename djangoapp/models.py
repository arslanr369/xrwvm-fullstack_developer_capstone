# Uncomment the following imports before adding the Model code
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add any other fields you may need
    # e.g., country_of_origin = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # Return the name as the string representation


# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-To-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )
    # Add any other fields you may need
    # e.g., price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # Return the make and model as the string representation
