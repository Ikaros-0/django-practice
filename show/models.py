from django.db import models

# Create your models here.

# 温度数据模型
class Temperature(models.Model):
    captime = models.DateTimeField(auto_now_add=False)
    captemperature = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.captemperature
    
# 二氧化碳数据模型
class co2(models.Model):
    captime = models.DateTimeField(auto_now_add=False)
    capco2 = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.capco2