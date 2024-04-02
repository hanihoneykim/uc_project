from django.urls import path
from cms import views

urlpatterns = [
    path(
        "channel/rate_management",
        views.RateManagementListView.as_view(),
        name="rate_management",
    ),
]
