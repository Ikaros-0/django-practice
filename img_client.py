# 模拟图片上传
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

url = 'http://127.0.0.1:8000/img/upload/' # 接收图片的地址
path = './2.jpg' # 图片路径
file = path

multipart_encoder = MultipartEncoder(
    fields={
    'upload':('2.jpg', open(file,'rb'), 'image/jpeg') # 文件名/文件/格式
    }
)

headers = {} # 请求头
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0', 
#     'Referer': url 
# }
headers['Content-Type'] = multipart_encoder.content_type # 请求格式
response = requests.post(url=url, data= multipart_encoder , headers = headers)