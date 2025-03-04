from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from kitchen.models import DishType, Dish, Cook


def index(request: HttpRequest) -> HttpResponse:
    num_dish_types = DishType.objects.all()
    num_dishes = Dish.objects.all()
    num_cooks = Cook.objects.all()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_visits": num_visits
    }
    return render(request, "index.html", context=context)