class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        # print('__eq__方法被调用了，other=',other)
        return  self.name == other.name and self.age == other.age  #从写这个方法

#调用__new__方法申请内存空间
p1 = Person('zangsan',18)

#调用__new__方法申请内存空间
p2 = Person('zangsan',18)

#P1 和P2不是一个内存空间
print(id(p1))
print(id(p2))

#身份运算符 is 可以用来判断两个对象是否是同一个对象
#== 调用调用__eq__方法，获取这个方法的比较结果 eq 方法默认比较的是内存地址
print(p1 is p2)
print(p1 == p2)

num1 = [1,2,3]
num2 = [1,2,3]
print(num1 is num2)