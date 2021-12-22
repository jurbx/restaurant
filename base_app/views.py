from django.shortcuts import render, redirect
from .models import Dish, CategoryDish, ModelFormRegistration
from .forms import FormRegistration


def base_app_view(request):
    if request.method == 'POST':
        form = FormRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        x = form.errors
        x = 2

    form_registration = FormRegistration()
    dishes = Dish.objects.filter(is_visible=True).order_by('dish_order')
    categories = CategoryDish.objects.filter(is_visible=True).order_by('position')
    special = Dish.objects.filter(is_special=True, is_visible=True).order_by('dish_order')
    return render(request, 'base_app.html', context={
        'dishes': dishes,
        'categories': categories,
        'special': special,
        'form_registration': form_registration
    })
