from django.db import models
from uuid import uuid4
from os import path
from django.core.validators import RegexValidator


class CategoryDish(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class Dish(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('image/dishes', filename)

    name = models.CharField(unique=True, max_length=50, db_index=True)
    dish_order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    ingredients = models.TextField(max_length=400)
    photo = models.ImageField(upload_to=get_file_name)
    desc = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(CategoryDish, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return f'{self.name}: {self.price}'


class ModelFormRegistration(models.Model):
    mobile_regex = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone format xxx xxx xxxx')
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10, validators=[mobile_regex])
    date = models.DateField()
    time = models.DateTimeField()
    count_of_people = models.PositiveIntegerField()
    message = models.TextField(max_length=400, blank=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-time', )

    def __str__(self):
        return f'{self.name}, {self.email}, {self.phone}'
