from django.urls import path

from . import views

urlpatterns = [
    path("", views.dispatchers_list, name="dispatchers_list"),
    path("<int:pk>/", views.dispatcher_detail, name="dispatcher_detail"),
    path("create/", views.dispatcher_create, name="dispatcher_create"),
    path("<int:pk>/edit/", views.dispatcher_update, name="dispatcher_update"),
    path("<int:pk>/delet/", views.dispatcher_delete, name="dispatcher_delete"),
]
