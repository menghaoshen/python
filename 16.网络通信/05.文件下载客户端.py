import  socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9090))

# s.send('hello'.encode('utf8'))
fiel_name = input('请输入你要下载的文件名：')
s.send(fiel_name.encode('utf8'))


with open(fiel_name + "1",'wb') as file:
    while True:  #数据超过1k 不停的写到文件里面
        content = s.recv(1024)
        if not content:
            break
        file.write(content)


s.close()