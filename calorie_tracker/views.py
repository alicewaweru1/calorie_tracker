from django.shortcuts import render, redirect
from .models import FoodItem
from .forms import FoodForm

def home(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = FoodForm()

    foods = FoodItem.objects.all()
    total_calories = sum(food.calories for food in foods)

    context = {
        "form": form,
        "foods": foods,
        "total_calories": total_calories,
    }

    return render(request, "calorie_tracker/home.html", context)