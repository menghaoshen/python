import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定地址和端口好
s.bind(('127.0.0.1',9090))

#recvform 接收数据
# content = s.recvfrom(1024)
#接受到数据是个元组，元组里面有两个元素
#第0个是接受到的数据， #第一个元素是发送方的ip地址和端口好
data,addr = s.recvfrom(1024) # recvform 是一个阻塞的方法，等待
print('从{}地址{}端口号接受到了消息，内容是:{}'.format(addr[0],addr[1],data.decode('utf8')))
s.close()
