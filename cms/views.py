from django.shortcuts import render
from rest_framework import generics, status


class RateManagementListView(generics.ListCreateAPIView):
    template_name = "pages/cms/rate_management.html"

    def get(self, request):
        user = request.user
        return render(request, "pages/cms/rate_management.html", {"user": user})
