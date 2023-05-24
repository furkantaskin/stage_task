from django.db import models
import datetime
from uuid import uuid4


class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=40)
    plate_number = models.CharField(max_length=10, unique=True)
    year = models.PositiveIntegerField(default=datetime.date.today().year)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.plate_number


class Operation(models.Model):
    __operation_code = f"{datetime.date.today().strftime('%Y%m%d')}-{uuid4()}"
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    operation_date = models.DateField(default=datetime.date.today())
    description = models.TextField()
    operation_code = models.TextField(default=__operation_code)

    def __str__(self):
        return f"{self.car.plate_number} - {self.operation_date}"