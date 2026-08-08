from django.urls import path

from . import views



urlpatterns = [
    path("", views.fleet_list, name="fleetlist"),
    path("<int:pk>/", views.fleet_detail, name="fleet_detail"),
]
