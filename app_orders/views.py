from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Orders
from .forms import OrdersForm


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
    error = ""
    if request.method == "POST":
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            error = "Форма невалидна"
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
        print(code)
        if code == "12346":
            return HttpResponse('{"result": "true"}')
        else:
            return HttpResponse('{"result": "false"}')
