from django.urls import path

from . import views



urlpatterns = [
    path("", views.fleet_list, name="fleetlist"),
    path("<int:pk>/", views.fleet_detail, name="fleet_detail"),
    path('create/',views.fleet_create, name="fleet_create"),
    path("<int:pk>/edit/", views.fleet_update, name="fleet_update"),
    path("<int:pk>/delet/", views.fleet_delete, name='fleet_delete')
]
