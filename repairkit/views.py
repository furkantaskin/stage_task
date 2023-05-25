import django.db.utils
import datetime
from django.shortcuts import render, redirect
from .models import Car, Operation
from .forms import EditForm


def home(request):
    cars = Car.objects.all()
    operations = Operation.objects.all()
    return render(request, 'repairkit/home.html', {'cars': cars, 'operations': operations})


def cars(request):
    cars = Car.objects.all()
    return render(request, 'repairkit/cars.html', {'cars': cars})


def add_car(request):
    if request.method == "POST":
        try:
            brand = request.POST.get("brand")
            model = request.POST.get("model")
            year = request.POST.get("year")
            color = request.POST.get("color")
            plate = request.POST.get("plate")
            car = Car(brand=brand, model=model, plate_number=plate, color=color, year=year)
            car.save()
            return redirect("cars")
        except django.db.utils.IntegrityError:
            return render(request, "repairkit/add_car.html", {"error_message": "Bu plaka numarası ile zaten kayıt var"})
    else:
        return render(request, 'repairkit/add_car.html')

def operations(request, car_id):
    car = Car.objects.get(id=car_id)
    operation = Operation.objects.filter(car=car)
    return render(request, 'repairkit/operations.html', {'operations': operation, 'car': car})


def add_operation(request):
    if request.method == "POST":
        operation_date = request.POST.get("date") if request.POST.get("date") else datetime.date.today()
        car_id = request.POST.get("car")
        car = Car.objects.get(id=car_id)
        description = request.POST.get("desc")
        operation = Operation(car=car, description=description, operation_code=Operation.get_operation_code,
                              operation_date=operation_date)
        operation.save()
        return redirect("operations", car_id=car_id)
    else:
        cars = Car.objects.all()
        return render(request, 'repairkit/add_operation.html', {"cars": cars})


def delete_operation(request, operation_id):
    operation = Operation.objects.get(id=operation_id)
    print("Delete operation", operation)
    car_id = operation.car.id
    operation.delete()
    return redirect("operations", car_id=car_id)


def edit_operation(request, operation_id):
    operation = Operation.objects.get(id=operation_id)
    if request.method == "POST":
        form = EditForm(request.POST, instance=operation)
        if form.is_valid():
            form.save()
            return redirect("operations", car_id=operation.car.id)
    return render(request, "repairkit/edit_operation.html", {"form": EditForm(instance=operation)})