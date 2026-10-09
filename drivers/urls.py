from django.urls import path

from . import views


urlpatterns = [
    path("", views.drivers_list, name="drivers_list"),
    path("<int:pk>/", views.driver_detail, name="driver_detail"),
    path('create/',views.driver_create, name="driver_create"),
    path("<int:pk>/edit/", views.driver_update, name="driver_update"),
    path("<int:pk>/delet/", views.driver_delete, name='driver_delete')

]
