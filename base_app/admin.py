from django.contrib import admin
from .models import Dish, CategoryDish, ModelFormRegistration


@admin.register(Dish)
class DishesAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'dish_order', 'is_special', 'desc', 'photo', 'category', 'ingredients']
    list_filter = ['is_special', 'category']
    list_editable = ['price', 'is_special']


@admin.register(CategoryDish)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_visible', 'position']


admin.site.register(ModelFormRegistration)
