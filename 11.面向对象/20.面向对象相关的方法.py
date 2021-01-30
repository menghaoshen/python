class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
class X(object):
    pass
class Student(Person,X):
    pass



p1 = Person('张三',18)
p2 = Person('张三',18)
s = Student('jack',19)

print(p1 is p2) #is 身份运算符是用来比较是否是同一个对象
print(type(s) == Student) #True
print(type(s) == Person)  #False
# isinstance  用来判断一个对象是否是由指定的类，(或者子类)，实例化出来的
print(isinstance(s,(Student,X))) #可以写两个类
print(isinstance(s,Person))
print(isinstance(p1,Person))
print(isinstance(p1,Student))

# issubclass 用来判断一个类是否是另一个类的子类
print(issubclass(Student,Person))
print(issubclass(Person, Student))