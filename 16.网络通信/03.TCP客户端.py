import socket

# 基于tcp 的soccket 连接
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 在发送数据浅，必须要先和服务器建立连接
s.connect(('127.0.0.1',9090))

s.send('hello'.encode('utf8'))
