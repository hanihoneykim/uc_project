from django.urls import path
from pms import views

urlpatterns = [
    path("express/express", views.express, name="express"),
    path("express/room_available", views.room_available, name="room_available"),
    path("express/room_indicator", views.room_indicator, name="room_indicator"),
    path(
        "express/actual_arrival_list",
        views.ActualArrivalListView.as_view(),
        name="actual_arrival_list",
    ),
    path(
        "express/actual_departure_list",
        views.ActualDepartureListView.as_view(),
        name="actual_departure_list",
    ),
    path(
        "express/expected_arrival_list",
        views.ExpectedArrivalListView.as_view(),
        name="expected_arrival_list",
    ),
    path(
        "express/expected_departure_list",
        views.ExpectedDepartureListView.as_view(),
        name="expected_departure_list",
    ),
    path(
        "express/global_guest_list",
        views.GlobalGuestListView.as_view(),
        name="global_guest_list",
    ),
    path(
        "express/inhouse_list",
        views.InHouseListView.as_view(),
        name="inhouse_list",
    ),
    path(
        "express/reservation_list",
        views.ReservationListView.as_view(),
        name="reservation_list",
    ),
    path(
        "cashiering/night_audit",
        views.NightAudit.as_view(),
        name="night_audit",
    ),
    path(
        "house_keeping/out_of_order",
        views.OutOfOrder.as_view(),
        name="out_of_order",
    ),
]
