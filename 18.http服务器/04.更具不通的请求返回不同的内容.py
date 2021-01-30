import  socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('192.168.1.191',8080))
server_socket.listen(128) #队列等待的长度


while True:
    client_socket,client_addr = server_socket.accept()
    data = client_socket.recv(1024).decode('utf8')
    # print('接受到数据{}'.format(data))
    if data:
        path = data.splitlines()[0].split(' ')[1]
        print('请求的路径是{}'.format(path))
    # 响应体
    response_body = 'hello world'
    response_header = 'HTTP/1.1 404 Page Not Found'
    if path == '/login':
        response_body = '欢迎来到登录页面'
    elif path == '/register':
        response_body = '欢迎来到注册页面'
    elif path == '/':
        response_body = '欢迎来到首页'
    else:
        response_header = 'HTTP/1.1 404 Page not Found\n'
        response_body = '对不起，您要查找的页面不存在'
    #响应头
    response_header += 'content-type:text/html;charset=utf8\n'
    response_header += '\n'



    #响应
    response = response_header + response_body
    client_socket.send(response.encode('utf8'))