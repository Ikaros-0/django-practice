from django.shortcuts import render
from img.models import IMG
# Create your views here.

def showimg(request):
    srcs = IMG.objects.all()
    res = []
    for i in srcs:
        res.append(i.img)
    src = str(res[-1])
    src = '/media/' + src
    return render(request,'img/index.html', locals())