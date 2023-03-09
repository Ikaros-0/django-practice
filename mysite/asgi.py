import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from . import routings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webSocket.settings')
 
# 支持http请求和websocket请求
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(routings.websocket_urlpatterns)
})