#ASCII ==> Latin1 ==> uniconde 编码
#字符 --> 数字编码存在一个对于的关系

#使用内置函数chr 和ord能够查看数字和字符的对于关系
print(ord('a')) #根据字符获取对于的编码
print(chr(65))  #获取字符对于的编码

#GUBK UTF-8 BIG5
#字符串转换成指定编码集结果
#GBK编码,一个汉字占2个字节
print('你'.encode('gbk')) #b'\xc4\xe3'
#utf8一个汉族占三个字节
print('你'.encode('utf8')) #b'\xe4\xbd\xa0'
#解码utf8
x = b'\xe4\xbd\xa0'
print(x.decode('utf8'))
#乱码的原因就是编码和解码的格式不一样