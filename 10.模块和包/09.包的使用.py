#可以将多个相同或者相似或有关联的模块，放到一个文件夹里面，便于管理
#这个文件夹我们称之为包
#在python包里面，会有一个__init__ 文件

#从包里面导入模块
from chat import recv_msg
print(recv_msg.y)

#从包里面的模块，导入变量
from  chat.send_msg import x
print(x)