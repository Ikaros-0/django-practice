from django.shortcuts import render, HttpResponse
from img.models import IMG
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os
# Create your views here.

def showimg(request):
    srcs = IMG.objects.all()
    res = []
    for i in srcs:
        res.append(i.img)
    src = str(res[-1])
    src = '/media/' + src
    return render(request,'img/index.html', locals())

@csrf_exempt
def upload(request):
    if request.method == 'GET':
        return render(request, 'img/upload.html')
    else:
        imgobj = request.FILES.get('upload')
        fname = os.path.join(settings.MEDIA_ROOT, imgobj.name)
        # print(fname)
        # with open(fname, 'wb') as rfile:
        #     data = imgobj.file.read()
        #     rfile.write(data)
        image = IMG()
        image.img = request.FILES.get('upload')
        image.save()
    
        return HttpResponse('上传成功')