import datetime
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__money = 1000 #两个下划线开始的变量，是私有的变量
    #
    # def test(self):
    #     self.__money += 10 #在这里可以访问私有属性

    def get_money(self):
        #里面可以记录很多东西
        print('{}查询余额'.format(datetime.datetime.now()))
        return  self.__money

    def set_money(self,qian):
        if type(qian) != int: #可以判断输入的内容
            print('设置的余额不合法')
        print('修改余额了')
        self.__money = qian
        return  self.__money

    def __test(self): #两个下划线开始的函数,是私有函数,在外部无法调用
        print('我是test函数,name = {}'.format(self.name))

    def demon(self):
        self.__test()


p = Person('张三',18)

# p.test()
print(p.name,p.age) #可以直接获取
# print(p.__money)  #不能直接获取私有变量


#获取私有变量的方式：
#1. 使用对象._类名__私有变量名获取
print(p._Person__money)
#2.定义get和set方法可以获取
print(p.get_money())
print(p.set_money('hello'))

#私有函数不能直接调用,是私有的方法
# p.__test()
p._Person__test()  #硬调用