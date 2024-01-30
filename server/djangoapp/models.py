from django.db import models
from django.utils.timezone import now


# Create your models here.


class CarMake(models.Model):
    # Car Make model
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    # Car Model model
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()  # Assuming dealer_id is an integer, you can adjust the field type accordingly
    TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'WAGON'),
        # Add more choices as needed
    ]
    car_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    year = models.DateField()
    # Add other fields as needed

    def __str__(self):
        return f"{self.car_make} - {self.name}"

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
