from django.urls import path

from . import views

urlpatterns = [
    path("", views.work_order_list, name="work_order_list"),
    path("create/", views.work_order_create, name="work_order_create"),
    path("<int:pk>/", views.work_order_detail, name="work_order_detail"),
    path("<int:pk>/edit/", views.work_order_update, name="work_order_update"),
    path("<int:pk>/assign/", views.work_order_assign, name="work_order_assign"),
    path("<int:pk>/start/", views.work_order_start, name="work_order_start"),
    path("<int:pk>/complete/", views.work_order_complete, name="work_order_complete"),
    path("<int:pk>/cancel/", views.work_order_cancel, name="work_order_cancel"),
]
