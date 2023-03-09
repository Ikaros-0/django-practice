from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from show.models import Temperature
from show.serializers import TempSerializer
from rest_framework import generics

# Create your views here.

def index(request):
    return render(request, 'show/index.html')

class temperature_api(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TempSerializer

def temperature(request):
	data = Temperature.objects.all()
	res=[]
	if data:
		for i in data:
			tx=i.captime
			ty=i.captemperature
			res.append( [tx.isoformat(), float(ty)] )
	res = res[::-1][0:15]
	return render(request, 'show/temperature_index.html',locals()) 

def get_temperature(request):
	data = Temperature.objects.all()
	res=[]
	if data:
		for i in data:
			tx=i.captime
			ty=i.captemperature
			res.append( {"time":tx.isoformat(), "Temperature":float(ty) })
	return JsonResponse({'s1':res})