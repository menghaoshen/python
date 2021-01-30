#将数据写入到内存，设计String IO和BytesIO 两个类
from  io import  StringIO,BytesIO
s_io =  StringIO()
s_io.write('hello') #把数据写入到内存缓存起来
s_io.write('good')
print(s_io.getvalue())
s_io.close()
print('hello',file=open('sss.txt','w')) #写到文件里面
print('goo',file=s_io) #写到内存里面
print(s_io.getvalue())

b_io = BytesIO() #要用二进制
b_io.write('您好'.encode('utf8'))
print(b_io.getvalue().decode('utf8'))
b_io.close()