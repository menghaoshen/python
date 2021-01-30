#python里面存储数据，只支持字符串和二进制
#json： 将python里面的数据（str,list,tuple,dict,int,float,boot,None）等转换成对应的josn字符串
#pickle： 将python里面的任意对象转换成二进制

import pickle

#序列化    dumps ： 将python数据转换成为二进制
#         dump ：  将python数据转换成为二进制，同时保存到指定的文件
#反序列化： loads:  将二进制加载成为python数据
#         load：   读取文件，并将文件的二进制内容加载成为python数据

names = ['jcak','tom','lisi']
# b_names = pickle.dumps(names)
# print(b_names)
#
# file = open('name.txt','wb')
# file.write(b_names)  #写入的是二进制，不是纯文本，
# file.close()

#加载出来
# file1 = open('name.txt','rb')
# x = file1.read()
# y = pickle.loads(x)
# print(y)
# file1.close()

# file2 = open('name.txt','wb')
# pickle.dump(names,file2)
# file2.close()
#
# file3 = open('name.txt','rb')
# y = pickle.load(file3)
# print(y)

class Dog(object):
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def eat(self):
        print(self.name + '正在吃东西')

d = Dog('大黄','白色')
#保存到文件里面
pickle.dump(d,open('dog.txt','wb'))
# 从文件里面加载出来
dd = pickle.load(open('dog.txt','rb'))
dd.eat() #pickle 用来将数据原封不动的转换成二进制，但是这个二进制只能在python里面识别
print(dd.name,dd.color)


######################
# pickle 和 json 的区别，什么情况下面使用josn，什么情况下面使用pickle
# pickle 用来将数据原封不动的转换成二进制，但是这个二进制只能在python里面识别，不能跨平台传递
# json 只能保持一部分信息,作用是用来在不同的平台里传递数据
# json 里面存储的数据都是基本的数据类型
import  json
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name + '正在吃东西')

p = Person('henry',20)

x = json.dumps(p.__dict__) #转换完成以后eat方法就没有了
y = json.loads(x)
print(x)