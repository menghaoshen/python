#定义一个类属性,记录了创建了多少个对象

class Person(object):
    count = 0

    def __init__(self,name,age):
        Person.count += 1
        self.name = name
        self.age = age



#每次创建对象,都会调用__new__和__init__方法
p1 = Person('张三',18)
p2 = Person('李四',19)
p3 = Person('jack',19)

print(Person.count)