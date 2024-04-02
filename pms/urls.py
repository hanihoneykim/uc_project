from django.urls import path
from pms import views

urlpatterns = [
    path("express/express", views.express, name="express"),
    path("express/room_available", views.room_available, name="room_available"),
    path("express/room_indicator", views.room_indicator, name="room_indicator"),
    path(
        "express/actual_arrival_list",
        views.ActualArrivalList.as_view(),
        name="actual_arrival_list",
    ),
    path(
        "express/actual_departure_list",
        views.ActualDepartureList.as_view(),
        name="actual_departure_list",
    ),
]
