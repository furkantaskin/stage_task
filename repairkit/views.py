from django.shortcuts import render, redirect
from .models import Car, Operation


def home(request):
    cars = Car.objects.all()
    operations = Operation.objects.all()
    return render(request, 'repairkit/home.html', {'cars': cars, 'operations': operations})


def cars(request):
    cars = Car.objects.all()
    return render(request, 'repairkit/cars.html', {'cars': cars})


def add_car(request):
    if request.method == "POST":
        brand = request.POST.get("brand")
        model = request.POST.get("model")
        year = request.POST.get("year")
        color = request.POST.get("color")
        plate = request.POST.get("plate")

        print(f"Model adı: {model}")
        car = Car(brand=brand, model=model, plate_number=plate, color=color, year=year)
        car.save()
        return redirect("home")
    else:
        return render(request, 'repairkit/add_car.html')
