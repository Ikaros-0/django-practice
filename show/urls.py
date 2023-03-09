from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display', views.temperature,name='sensor.temperature'),
    path('temperature_api', views.temperature_api.as_view(),name='show.temperature_api'),
    path('get_temperature', views.get_temperature,name='sensor.get_temperature'),
]