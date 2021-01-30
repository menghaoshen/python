#不用继承的写法
# class Aniaml(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         print(self.name + '正在睡觉')
# class Dog(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         print(self.name + '正在睡觉')
#     def bark(self):
#         print(self.name + '正在叫')
# class Student(object):
#     def __init__(self,name,age):
#         self,name = name
#         self.age = age
#     def sleep(self):
#         print(self.name +'正在睡觉')
#     def study(self):
#         print(self.name + '正在学习')
#
#用继承的写法
class Aniaml(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sleep(self):
        print(self.name + '正在睡觉')

class Dog(Aniaml):
    def bark(self):
        print(self.name + '正在叫')
class Student(Aniaml):
    def study(self):
        print(self.name + '正在学习')

#Dog() 调用__new__方法,在调用__init__方法
#DOG() 里没有__new__方法,会查看父类是否重写__new__方法
#父类里面也没有重写__new__方法,会查找父类的父类,找到object
#调用__init方法
d1 = Dog('大黄',7)
print(d1.name) #父类定义的属性,子类可以直接使用
d1.sleep()  #父类的方法子类实例对象可以直接调用
d1.bark()

#子类可以用父类的对象
#但是子类直接不能调用,子类和子类没有关系
s1 = Student('小明',18)
s1.sleep()
s1.study()