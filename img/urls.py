from django.urls import path
from . import views

urlpatterns = [
    path('', views.showimg, name='index'),
    path('upload/', views.upload, name='img.upload'),
]