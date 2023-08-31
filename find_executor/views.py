from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "find_executor/index.html")


def about(request):
    return render(request, "find_executor/about.html")
