from django.urls import  re_path, path
from show.consumers import ChatConsumer
websocket_urlpatterns = [
    path('show/',ChatConsumer.as_asgi()),
    #也可以使用正则路径,这种方式用在群组通信当中
    re_path('ws/show/(?P<group>\w+)/$',ChatConsumer)
]