from django.urls import path
from cms import views

urlpatterns = [
    path(
        "channel/rate_management",
        views.RateManagementListView.as_view(),
        name="rate_management",
    ),
    path(
        "channel/room_inventory_management",
        views.RoomInventoryManagement.as_view(),
        name="room_inventory_management",
    ),
]
