from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display', views.display,name='show.display'),
    path('temperature_api', views.temperature_api.as_view(),name='show.temperature_api'),
    path('co2_api', views.co2_api.as_view(), name='show.co2_api'),
    path('humidity_api', views.humidity_api.as_view(), name='show.humidity_api'),
    path('get_temperature', views.get_temperature,name='show.get_temperature'),
    path('get_co2', views.get_co2, name='show.get_co2'),
    path('get_humidity', views.get_humidity, name='show.get_humidity'),
]