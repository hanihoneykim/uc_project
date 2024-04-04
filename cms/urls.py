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
    path(
        "channel/product_inventory_management",
        views.ProductInventoryManagement.as_view(),
        name="product_inventory_management",
    ),
    path(
        "channel/making_rate_package",
        views.RatePackageCreate.as_view(),
        name="making_rate_package",
    ),
    path(
        "channel/channel_information_configuration",
        views.ChannelInformationConfiguration.as_view(),
        name="channel_information_configuration",
    ),
    path(
        "channel/channel_management",
        views.ChannelManagement.as_view(),
        name="channel_management",
    ),
    path(
        "channel/data_synchronization",
        views.DataSynchronization.as_view(),
        name="data_synchronization",
    ),
    path(
        "channel/remaining_room_availability",
        views.RemainingRoomAvailability.as_view(),
        name="remaining_room_availability",
    ),
]
