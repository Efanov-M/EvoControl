from django.urls import path

from . import views


urlpatterns = [
    path("", views.vehicle_list, name="vehicle_list"),
    path("<int:pk>/", views.vehicle_detail, name="vehicle_detail"),
    path('create/',views.vehicle_create, name="vehicle_create"),
    path("<int:pk>/edit/", views.vehicle_update, name="vehicle_update"),
    path("<int:pk>/delet/", views.vehicle_delete, name='vehicle_delete')

]
