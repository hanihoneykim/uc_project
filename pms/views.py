from django.shortcuts import render
from datetime import date
from rest_framework import generics, status
from .models import Room, Reservation, CheckInOutStatus
from django.core.paginator import Paginator


class ExpressListView(generics.ListCreateAPIView):
    template_name = "pages/pms/express.html"

    def get(self, request):
        room_0 = Room.objects.all()[0]
        room_1 = Room.objects.all()[1]
        room_2 = Room.objects.all()[2]
        room_3 = Room.objects.all()[3]
        room_4 = Room.objects.all()[4]
        room_5 = Room.objects.all()[5]
        room_6 = Room.objects.all()[6]
        room_7 = Room.objects.all()[7]
        user = request.user
        return render(
            request,
            "pages/pms/express.html",
            {
                "user": user,
                "room_0": room_0,
                "room_1": room_1,
                "room_2": room_2,
                "room_3": room_3,
                "room_4": room_4,
                "room_5": room_5,
                "room_6": room_6,
                "room_7": room_7,
            },
        )


class RoomAvailableListView(generics.ListCreateAPIView):
    template_name = "pages/pms/room_available.html"

    def get(self, request):
        user = request.user
        rooms = Room.objects.all()
        user = request.user
        paginator = Paginator(rooms, 10)
        page_number = request.GET.get("page", "1")
        paging = paginator.get_page(page_number)
        return render(
            request, "pages/pms/room_available.html", {"user": user, "paging": paging}
        )


class RoomIndicatorListView(generics.ListCreateAPIView):
    template_name = "pages/pms/room_indicator.html"

    def get(self, request):
        user = request.user
        rooms = Room.objects.all()
        user = request.user
        paginator = Paginator(rooms, 10)
        page_number = request.GET.get("page", "1")
        paging = paginator.get_page(page_number)
        return render(
            request, "pages/pms/room_indicator.html", {"user": user, "paging": paging}
        )


class ActualArrivalListView(generics.ListCreateAPIView):
    template_name = "pages/pms/actual_arrival_list.html"

    def get(self, request):
        user = request.user
        check_in = CheckInOutStatus.objects.filter(check_in_out_status="in")
        paginator = Paginator(check_in, 10)
        page_number = request.GET.get("page", "1")
        paging = paginator.get_page(page_number)
        return render(
            request,
            "pages/pms/actual_arrival_list.html",
            {"user": user, "paging": paging},
        )


class ActualDepartureListView(generics.ListCreateAPIView):
    template_name = "pages/pms/actual_departure_list.html"

    def get(self, request):
        user = request.user
        check_in = CheckInOutStatus.objects.filter(check_in_out_status="out")
        paginator = Paginator(check_in, 10)
        page_number = request.GET.get("page", "1")
        paging = paginator.get_page(page_number)
        return render(
            request,
            "pages/pms/actual_departure_list.html",
            {"user": user, "paging": paging},
        )


class ExpectedArrivalListView(generics.ListCreateAPIView):
    template_name = "pages/pms/expected_arrival_list.html"

    def get(self, request):
        user = request.user
        today = date.today()
        check_in = CheckInOutStatus.objects.filter(
            check_in_out_status__isnull=True, reservation__check_in_date=today
        )
        paginator = Paginator(check_in, 10)
        page_number = request.GET.get("page", "1")
        paging = paginator.get_page(page_number)
        return render(
            request,
            "pages/pms/expected_arrival_list.html",
            {"user": user, "paging": paging},
        )


class ExpectedDepartureListView(generics.ListCreateAPIView):
    template_name = "pages/pms/expected_departure_list.html"

    def get(self, request):
        user = request.user
        return render(request, "pages/pms/expected_departure_list.html", {"user": user})


class GlobalGuestListView(generics.ListCreateAPIView):
    template_name = "pages/pms/global_guest_list.html"

    def get(self, request):
        user = request.user
        return render(request, "pages/pms/global_guest_list.html", {"user": user})


class InHouseListView(generics.ListCreateAPIView):
    template_name = "pages/pms/inhouse_list.html"

    def get(self, request):
        user = request.user
        return render(request, "pages/pms/inhouse_list.html", {"user": user})


class ReservationListView(generics.ListCreateAPIView):
    template_name = "pages/pms/reservation_list.html"

    def get(self, request):
        user = request.user
        return render(request, "pages/pms/reservation_list.html", {"user": user})


class NightAudit(generics.ListCreateAPIView):
    template_name = "pages/pms/night_audit.html"

    def get(self, request):
        user = request.user
        return render(request, "pages/pms/night_audit.html", {"user": user})


class OutOfOrder(generics.ListCreateAPIView):
    template_name = "pages/pms/out_of_order.html"

    def get(self, request):
        user = request.user
        return render(request, "pages/pms/out_of_order.html", {"user": user})
