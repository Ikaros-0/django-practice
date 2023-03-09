from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from show.models import Temperature, co2
from show.serializers import TempSerializer, Co2Serializer
from rest_framework import generics

# Create your views here.
# 主页
def index(request):
    return render(request, 'show/index.html')

# 温度
class temperature_api(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TempSerializer

def get_temperature(request):
	data = Temperature.objects.all()
	res=[]
	if data:
		for i in data:
			tx=i.captime
			ty=i.captemperature
			res.append( {"time":tx.isoformat(), "Temperature":float(ty) })
	return JsonResponse({'s1':res})


# 二氧化碳
class co2_api(generics.ListCreateAPIView):
	queryset = co2.objects.all()
	serializer_class = Co2Serializer

def get_co2(request):
	data = co2.objects.all()
	res = []
	if data:
		for i in data:
			tx = i.captime
			ty = i.capco2
			res.append({"time":tx.isoformat(), "co2":float(ty) })
	return JsonResponse({"s1":res})


def display(request):
	# 温度
	data1 = Temperature.objects.all()
	res1=[]
	if data1:
		for i in data1:
			tx=i.captime
			ty=i.captemperature
			res1.append( [tx.isoformat(), float(ty)] )
	res1 = res1[::-1][0:15][::-1]
	# 二氧化碳
	data2 = co2.objects.all()
	res2 = []
	if data2:
		for j in data2:
			nx = j.captime
			ny = j.capco2
			res2.append([nx.isoformat(), float(ny)])
	res2 = res2[::-1][0:15][::-1]

	return render(request, 'show/temperature_index.html',locals()) 