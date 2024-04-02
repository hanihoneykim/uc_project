from django.shortcuts import render


def index(request):
    user = request.user
    return render(request, "pages/index.html", {"user": user})
