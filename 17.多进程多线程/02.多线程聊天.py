import  socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto('早上好'.encode('utf8'),('127.0.0.1',9090))

#data 的数据类型是一个元组
#元组的第0个元素是接收到的元组
#元组里第1个元素是发送方的ip地址和端口号
data = s.recvfrom(1024)
print(data)

s.close()