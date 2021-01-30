# python 里面使用open 内置函数打开并操作一个文件
# open  参数介绍
# file 用来指定打开的文件，不是文件的名字，是文件的路径
# mode 打开文件时的模式，默认是r，表示自读
# encoding： 打开文件时的编码方式
# r: 只读模式，默认，打开文件以后，只能读取，不能写入,如果文件不存在，会报错
# w: 写入模式：打开文件以后，只能写入，不能读取,如果文件存在，会覆盖，如果文件不存在，会创建
# b： 二进制形式，打开文件，操作非文本文件
# rb： 二进制读取
# wb： 二进制写入
# a 追加模式，会在文本的最后追加内容，如果文件不存在，会创建文件，如果文件存在，会在文本后面追加内容
# r+： 可读可写
# w+： 可写读

# r w 的方式
# file = open('./file1.txt','r')
# print(file.read())
# # file.write('hello')  #不能写，会报错
# file.close()

# file = open('./file1.txt','w')
# print(file)
# file.write('hello')
# file.close()

# 二进制的方式
# file = open('./file.txt','rb')
# print(file.read())
# file.close()
#
# file = open('file.txt','wb')
# file.write('大家好才是真的好'.encode('utf8'))
# file.close()
#

# file = open('./file.txt', 'w+')
# file.write('哈哈')
# file.seek(0,0) #需要重新重置文件指针
# print(file.read())
# file.close()
file = open('file.txt',encoding='gbk')
# print(file.read()) #将所有的数据读出来
# print(file.readline()) #读一行数
print(file.read(10))  #指读取的长度
# print(file.readlines()) #将所有行的数据都读取，保存到一个列表里面
# while True:
#     content = file.readline()
#     print(content)
#     if content == '':
#         break
file.close()



