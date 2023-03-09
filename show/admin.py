from django.contrib import admin

# Register your models here.
from .models import *

class TemperatureAdmin(admin.ModelAdmin):
	list_display = ('id','captime','captemperature')
admin.site.register(Temperature,TemperatureAdmin)