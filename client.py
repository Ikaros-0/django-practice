import json
import datetime
import requests
import random
from time import sleep

rqs_headers={'Content-Type': 'application/json'}
# requrl ='http://127.0.0.1:8000/show/temperature_api' #服务器的IP地址


class ComplexEncoder(json.JSONEncoder):#这个是用来把datetime的时间格式化
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


# temperature = random.randint(0,20)
# new_data = {
#     "captime": datetime.datetime.now(),
#     "captemperature": temperature
# }

# test_data = json.dumps(new_data, cls=ComplexEncoder)
# print(type(new_data))
# print(type(test_data))
# print(new_data)
# print(test_data)
        
flag = 1
while(1):

    sleep(2)
    print(flag)
    flag += 1

    # # 模拟温度数据
    # requrl ='http://127.0.0.1:8000/show/temperature_api' #服务器的IP地址
    # temperature = random.randint(0,20)
    # new_data = {
    #     "captime": datetime.datetime.now(),
    #     "captemperature": temperature
    # }

    # 模拟二氧化碳数据
    requrl ='http://127.0.0.1:8000/show/co2_api' #服务器的IP地址
    co2 = random.randint(0,20)
    new_data = {
        "captime": datetime.datetime.now(),
        "capco2": co2
    }

    test_data = json.dumps(new_data, cls=ComplexEncoder)
    print(type(new_data))
    print(test_data)

    response = requests.post(url=requrl, headers=rqs_headers, data=test_data)