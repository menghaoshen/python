import  socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('192.168.1.191',9090))
server_socket.listen(128) #队列等待的长度


while True:
    client_socket,client_addr = server_socket.accept()
    data = client_socket.recv(1024).decode('utf8')
    print('接受到数据{}'.format(data))
    client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
    client_socket.send('content-type:text/html\n'.encode('utf8'))
    client_socket.send('\n'.encode('utf8'))
    client_socket.send('<h1 style="color:red">hello world</h1>'.encode('utf8'))


"""
GET 请求的方式，GET/POST/PUT/DELETE
Host: 192.168.1.191:9090  请求服务的地址
idex.html   请求的路径和请求参数
Connection: keep-alive   
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
 UA 用户代理，最开始设计的目的，是为了能从请求头里面辨识浏览器的内容
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6

"""