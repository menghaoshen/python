import socket

# 创建一个socket 连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1',9090))

s.listen(128)  # 把socket 变成一个被动监听的socket
# 接受到的结果是一个元组，元组里面有两个元素
# 第0个元素是客户端的socket连接，第1个元素是客户端的ip地址和端口号
client,addr = s.accept()  # 接受客户端的请求
data = client.recv(1024) # #tcp 使用recv获取数据，1024 指的是获取数据的大写
print('接受到了{}客户端{}端口号发送的数据，内容是{}'.format(addr[0],addr[1],data.decode('utf8')))