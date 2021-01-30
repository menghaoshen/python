# python 里面使用open 内置函数打开并操作一个文件
# open  参数介绍
# file 用来指定打开的文件，不是文件的名字，是文件的路径
# mode 打开文件时的模式，默认是r，表示自读
# encoding： 打开文件时的编码方式

#open 函数会有一个返回值，打开文件对象
#在windows 系统里面，默认使用时的gbk编码格式打开文件
# 解决方案：读取和写入的编码格式一致即可
file = open('./file.txt',encoding='utf8')
# print(type(file))
print(file.read())

file.close() #操作完成后，要关闭文件