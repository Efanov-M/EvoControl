from django.urls import path

from . import views



urlpatterns = [
    path("", views.parking_list, name="parking_list"),
    path("<int:pk>/", views.parking_detail, name="parking_detail"),
]
