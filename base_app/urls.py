from django.urls import path
from .views import base_app_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base_app'

urlpatterns = [
    path('', base_app_view, name='base_app_view')
]