import json
import datetime
import requests
import random
from time import sleep

rqs_headers={'Content-Type': 'application/json'}

class ComplexEncoder(json.JSONEncoder):#这个是用来把datetime的时间格式化
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

flag = 1
while(1):

    sleep(2)
    print(flag)
    flag += 1

    # 模拟温度数据
    requrl_1 ='http://127.0.0.1:8000/show/temperature_api' #服务器的IP地址
    temperature = random.randint(0,20)
    new_data_1 = {
        "captime": datetime.datetime.now(),
        "captemperature": temperature
    }

    # 模拟二氧化碳数据
    requrl_2 ='http://127.0.0.1:8000/show/co2_api' #服务器的IP地址
    co2 = random.randint(0,20)
    new_data_2 = {
        "captime": datetime.datetime.now(),
        "capco2": co2
    }

    # 模拟湿度数据
    requrl_3 = 'http://127.0.0.1:8000/show/humidity_api' #服务器的IP地址
    humidity = random.randint(0,20)
    new_data_3 = {
        "captime": datetime.datetime.now(),
        "caphumidity": humidity
    }

    test_data_1 = json.dumps(new_data_1, cls=ComplexEncoder)
    test_data_2 = json.dumps(new_data_2, cls=ComplexEncoder)
    test_data_3 = json.dumps(new_data_3, cls=ComplexEncoder)

    response = requests.post(url=requrl_1, headers=rqs_headers, data=test_data_1)
    response = requests.post(url=requrl_2, headers=rqs_headers, data=test_data_2)
    response = requests.post(url=requrl_3, headers=rqs_headers, data=test_data_3)