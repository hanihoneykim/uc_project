from django.shortcuts import render
from rest_framework import generics, status


def express(request):
    user = request.user
    return render(request, "pages/pms/express.html", {"user": user})


def room_available(request):
    user = request.user
    return render(request, "pages/pms/room_available.html", {"user": user})


def room_indicator(request):
    user = request.user
    return render(request, "pages/pms/room_indicator.html", {"user": user})


class ActualArrivalListView(generics.ListCreateAPIView):
    template_name = "pages/pms/actual_arrival_list.html"

    def get(self, request):
        user = request.user
        return render(request, "pages/pms/actual_arrival_list.html", {"user": user})


class ActualDepartureListView(generics.ListCreateAPIView):
    template_name = "pages/pms/actual_departure_list.html"

    def get(self, request):
        user = request.user
        return render(request, "pages/pms/actual_departure_list.html", {"user": user})


class ExpectedArrivalListView(generics.ListCreateAPIView):
    template_name = "pages/pms/expected_arrival_list.html"

    def get(self, request):
        user = request.user
        return render(request, "pages/pms/expected_arrival_list.html", {"user": user})


class ExpectedDeparListView(generics.ListCreateAPIView):
    template_name = "pages/pms/expected_departure_list.html"

    def get(self, request):
        user = request.user
        return render(request, "pages/pms/expected_departure_list.html", {"user": user})
