from django.shortcuts import render
from rest_framework import generics, status
from pms.models import Reservation
from django.core.paginator import Paginator
from .models import RatePackage, Channel, CMSReservation, History, FAQ


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


class RatePackageCreate(generics.ListCreateAPIView):
    template_name = "pages/cms/making_rate_package.html"

    def get(self, request):
        user = request.user
        data_1 = RatePackage.objects.filter(room_type="스위트")
        data_2 = RatePackage.objects.filter(room_type="스위트노윈도우")
        data_3 = RatePackage.objects.filter(room_type="마루스위트")
        data_4 = RatePackage.objects.filter(room_type="패밀리스위트")
        return render(
            request,
            "pages/cms/making_rate_package.html",
            {
                "user": user,
                "data_1": data_1,
                "data_2": data_2,
                "data_3": data_3,
                "data_4": data_4,
            },
        )


class ChannelInformationConfiguration(generics.ListAPIView):
    template_name = "pages/cms/channel_information_configuration.html"

    def get(self, request):
        user = request.user
        return render(
            request, "pages/cms/channel_information_configuration.html", {"user": user}
        )


class ChannelManagement(generics.ListAPIView):
    template_name = "pages/cms/channel_management.html"

    def get(self, request):
        user = request.user
        channels = Channel.objects.all()
        return render(
            request,
            "pages/cms/channel_management.html",
            {"user": user, "channels": channels},
        )


class DataSynchronization(generics.ListAPIView):
    template_name = "pages/cms/data_synchronization.html"

    def get(self, request):
        user = request.user
        return render(
            request,
            "pages/cms/data_synchronization.html",
            {"user": user},
        )


class RemainingRoomAvailability(generics.ListAPIView):
    template_name = "pages/cms/remaining_room_availability.html"

    def get(self, request):
        user = request.user
        return render(
            request,
            "pages/cms/remaining_room_availability.html",
            {"user": user},
        )


class CMSReservationListView(generics.ListAPIView):
    template_name = "pages/cms/cms_reservation_list.html"

    def get(self, request):
        user = request.user
        cms_reservations = CMSReservation.objects.all()
        paginator = Paginator(cms_reservations, 30)
        page_number = request.GET.get("page", "1")
        paging = paginator.get_page(page_number)
        return render(
            request,
            "pages/cms/cms_reservation_list.html",
            {"user": user, "paging": paging},
        )


class RemainigRoomStatus(generics.ListAPIView):
    template_name = "pages/cms/remaining_room_status.html"

    def get(self, request):
        user = request.user
        # cms_reservations = CMSReservation.objects.all()
        # paginator = Paginator(cms_reservations, 30)
        # page_number = request.GET.get("page", "1")
        # paging = paginator.get_page(page_number)
        return render(
            request,
            "pages/cms/remaining_room_status.html",
            {"user": user},
        )


class SystemManagementHistory(generics.ListAPIView):
    template_name = "pages/cms/system_management_history.html"

    def get(self, request):
        user = request.user
        history = History.objects.all()
        paginator = Paginator(history, 30)
        page_number = request.GET.get("page", "1")
        paging = paginator.get_page(page_number)
        return render(
            request,
            "pages/cms/system_management_history.html",
            {"user": user, "paging": paging},
        )


class FAQListView(generics.ListAPIView):
    template_name = "pages/cms/faq.html"

    def get(self, request):
        user = request.user
        faq_1 = FAQ.objects.all()[0]
        faq_2 = FAQ.objects.all()[1]
        faq_3 = FAQ.objects.all()[2]
        faq_4 = FAQ.objects.all()[3]
        faq_5 = FAQ.objects.all()[4]

        return render(
            request,
            "pages/cms/faq.html",
            {
                "user": user,
                "faq_1": faq_1,
                "faq_2": faq_2,
                "faq_3": faq_3,
                "faq_4": faq_4,
                "faq_5": faq_5,
            },
        )
