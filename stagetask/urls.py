from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('repairkit/', include("repairkit.urls")),
    path('admin/', admin.site.urls),
]
