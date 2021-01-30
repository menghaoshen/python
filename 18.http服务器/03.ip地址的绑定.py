import  socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('192.168.1.191',9090))
# 127.0.01
# 0.0.0.0

server_socket.listen(128) #队列等待的长度


while True:
    client_socket,client_addr = server_socket.accept()
    data = client_socket.recv(1024).decode('utf8')
    print('接受到数据{}'.format(data))
    client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
    client_socket.send('content-type:text/html\n'.encode('utf8'))
    client_socket.send('\n'.encode('utf8'))
    client_socket.send('<h1 style="color:red">hello world</h1>'.encode('utf8'))