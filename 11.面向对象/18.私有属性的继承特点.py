class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000
    def eat(self):
        print(self.name + '正在吃东西')

    def __test(self):
        print('我是Animal类里面的test的方法')


class Person(Animal):
    def __demo(self):
        print('我是Person里的私有方法')


p = Person('张胜男', 18)
print(p.name)
print(p.eat())
# print(p.__test) #私有的方法，不能被调用
p._Person__demo()  #自己类里定义的私有方法，对象名._类名__私有方法名（）
p._Animal__test()  #可以通过 对象名._父类名__私有方法调用()
# p._Person__test() #父类的私有方法，子类没有继承

print(p._Person__money) #私有的属性，没有继承，无法调用
print(p._Animal__money)
