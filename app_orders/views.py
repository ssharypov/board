from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Orders
from .forms import OrdersForm
import time


# Create your views here.
def index(request):
    orders = Orders.objects.order_by("-id")
    paginator = Paginator(orders, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "app_orders/index.html",
        {
            # "orders": orders,
            "page_obj": page_obj,
        },
    )


def create(request):
    error = ""
    if request.method == "POST":
        form = OrdersForm(request.POST)
        if form.is_valid() and (len(request.POST.get("order_description")) > 99):
            form.save()
            return redirect("/")
        else:
            error = "Объявление пустое или слишком короткое"
            data = {
                "form": form,
                "error": error,
            }
            return render(request, "app_orders/create.html", data)
    else:
        form = OrdersForm()
        data = {
            "form": form,
            "error": error,
        }
        return render(request, "app_orders/create.html", data)


def check_code(request):
    if request.method == "POST":
        code = request.POST.get("code")
        # имитация ожидания
        time.sleep(3)
        if code == "12346":
            return HttpResponse('{"result": "true"}')
        else:
            return HttpResponse('{"result": "false"}')
