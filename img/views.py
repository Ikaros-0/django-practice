from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from img.models import IMG
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
import os
# Create your views here.

@never_cache
def showimg(request):
    srcs = IMG.objects.all()
    res = []
    for i in srcs:
        res.append({'time':i.captime, 'img':'/media/'+str(i.img)})
    if len(res) >= 6:
        src = res[::-1][0:6]
    else:
        src = res[::-1]
        while(len(src)<6):
            src.append({'time':'null', 'img': '/static/img/NULL.jpg'})
    return render(request,'img/index.html', locals())

@csrf_exempt
def upload(request):
    if request.method == 'GET':
        return render(request, 'img/upload.html')
    else:
        imgobj = request.FILES.get('upload')
        fname = os.path.join(settings.MEDIA_ROOT, imgobj.name)
        image = IMG()
        image.img = request.FILES.get('upload')
        image.save()
    
        return HttpResponse('上传成功')
    
def get_imgs(request):
    data = IMG.objects.all()
    res = []
    if data:
        for i in data:
            res.append({"time":i.captime, "img": '/media/'+str(i.img)})
    return JsonResponse({'s1':res})
