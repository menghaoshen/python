import  socket

#HTTP 服务器都是居于TCP的socket连接

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('192.168.1.191',9090))
server_socket.listen(128) #队列等待的长度

#获取的数据是一个元组
#第0个元素是客户端的socket连接
#第1个元素是客户端的ip地址和端口号

client_socket,client_addr = server_socket.accept()

#从客户端的socket 获取数据
data = client_socket.recv(1024).decode('utf8')
print('接受到数据{}'.format(data))
#返回内容之前，需要先设置http响应头
#设置一个响应头就换一行
client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
client_socket.send('content-type:text/html\n'.encode('utf8'))

#所有响应头设置完成后在换行
client_socket.send('\n'.encode('utf8'))

# 给客户端返回消息
client_socket.send('hello world'.encode('utf8'))
