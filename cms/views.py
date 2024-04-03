from django.shortcuts import render
from rest_framework import generics, status


class RateManagementListView(generics.ListCreateAPIView):
    template_name = "pages/cms/rate_management.html"

    def get(self, request):
        user = request.user
        return render(request, "pages/cms/rate_management.html", {"user": user})


class RoomInventoryManagement(generics.ListAPIView):
    template_name = "pages/cms/room_inventory_management.html"

    def get(self, request):
        user = request.user
        return render(
            request, "pages/cms/room_inventory_management.html", {"user": user}
        )


class ProductInventoryManagement(generics.ListAPIView):
    template_name = "pages/cms/product_inventory_management.html"

    def get(self, request):
        user = request.user
        return render(
            request, "pages/cms/product_inventory_management.html", {"user": user}
        )
