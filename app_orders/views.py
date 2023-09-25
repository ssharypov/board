from django.shortcuts import render
from .models import Orders


# Create your views here.
def index(request):
    orders = Orders.objects.order_by("-id")
    return render(
        request,
        "app_orders/index.html",
        {
            "orders": orders,
        },
    )


def create(request):
    return render(request, "app_orders/create.html")
