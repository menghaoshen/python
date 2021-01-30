# 不同电脑直接的通信使用socket
import socket
# 不同电脑直接的通信使用socket
# socket 可以在不同的电脑间通信，还可以在同一个电脑的不同程序之间通信
#1. 创建socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#2. 发送数据
# data 要发送的数据，它是二进制数据
# address ：发给谁，参数是一个元组，元组里有两个元素
#第0个表示目标的ip地址，第二个表示端口
#给自己的9000端口发送信息
s.sendto('您好'.encode('utf8'),('127.0.0.1',9090))

#接受消息
data,addr = s.recvfrom(1024)
print('从{}地址{}端口号接受到了消息，内容是:{}'.format(addr[0],addr[1],data.decode('utf8')))
#3. 关闭socket
s.close()

