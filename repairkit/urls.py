from django.urls import path
from .views import add_car, home, cars, operations, add_operation, delete_operation, edit_operation

urlpatterns = [
    path('', cars, name='index'),
    path('add_car', add_car, name='add_car'),
    path('home', home, name="home"),
    path('cars', cars, name="cars"),
    path('operations/<int:car_id>', operations, name="operations"),
    path('add_operation', add_operation, name="add_operation"),
    path('delete_operation/<int:operation_id>', delete_operation, name="delete_operation"),
    path('edit_operation/<int:operation_id>', edit_operation, name="edit_operation"),
]
