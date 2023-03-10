# 模拟图片上传
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
from time import sleep

url = 'http://127.0.0.1:8000/img/upload/' # 接收图片的地址

# 打开文件
path0 = "./imgs_test"
dirs = os.listdir( path0 )

headers = {} # 请求头

for file in dirs:
    path = path0 +'/'+ file
    fname = file
    multipart_encoder = MultipartEncoder(
        fields={
        'upload':(fname, open(path,'rb'), 'image/jpeg') # 文件名/文件/格式
        }
    )
    headers['Content-Type'] = multipart_encoder.content_type # 请求格式
    response = requests.post(url=url, data= multipart_encoder , headers = headers)
    sleep(5)