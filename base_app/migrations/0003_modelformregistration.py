# Generated by Django 4.0 on 2021-12-15 18:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelFormRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone format xxx xxx xxxx', regex='^(\\d{3}[- .]?){2}\\d{4}$')])),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('count_of_people', models.PositiveIntegerField()),
                ('message', models.TextField(blank=True, max_length=400)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date', '-time'),
            },
        ),
    ]
