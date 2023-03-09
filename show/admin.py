from django.contrib import admin

# Register your models here.
from .models import *

class TemperatureAdmin(admin.ModelAdmin):
	list_display = ('id','captime','captemperature')
admin.site.register(Temperature,TemperatureAdmin)

class Co2Admin(admin.ModelAdmin):
	list_display = ('id','captime','capco2')
admin.site.register(co2,Co2Admin)

class HumidityAdmin(admin.ModelAdmin):
	list_display = ('id','captime','caphumidity')
admin.site.register(humidity,HumidityAdmin)