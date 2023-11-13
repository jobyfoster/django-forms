from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from .forms import HeyYouForm, HowOldForm, OrderTotalForm

# Create your views here.


def hey_you_view(request: HttpRequest) -> HttpResponse:
    form = HeyYouForm()
    if request.GET:
        form = HeyYouForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data["name"]
            return render(request, "hey_you.html", context={"form": form, "name": name})

    return render(request, "hey_you.html", context={"form": form})


def how_old_view(request: HttpRequest) -> HttpResponse:
    form = HowOldForm()
    if request.GET:
        form = HowOldForm(request.GET)
        if form.is_valid():
            birth_year = form.cleaned_data["birth_year"]
            end = form.cleaned_data["end"]

            age = end - birth_year
            return render(
                request, "how_old.html", context={"form": form, "age": age, "end": end}
            )

    return render(request, "how_old.html", context={"form": form})


def order_total_view(request: HttpRequest) -> HttpResponse:
    form = OrderTotalForm()
    if request.GET:
        form = OrderTotalForm(request.GET)
        if form.is_valid():
            burgers = form.cleaned_data["burgers"]
            fries = form.cleaned_data["fries"]
            drinks = form.cleaned_data["drinks"]

            total = f"{(burgers * 4.5) + (fries * 1.5) + drinks:,.2f}"
            return render(
                request, "order_total.html", context={"form": form, "total": total}
            )

    return render(request, "order_total.html", context={"form": form})
