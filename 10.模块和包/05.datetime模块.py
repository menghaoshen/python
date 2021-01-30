import  datetime

#以一个下划线开始的 _
#以两个下划线__ 开始
#两个下划线开始两个下划线结束__dt__

print(datetime.datetime.now()) #拿到当前的时间
print(datetime.date(2020,1,1)) #创建一个时间
print(datetime.time(18,23,32)) #创建一个时间
print(datetime.datetime.now()) #获取当前时间
print(datetime.datetime.now() + datetime.timedelta(3)) #获取当前时间 #计算三天以后的时间

