class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __eq__(self, other):
        return  self.name == other.name and self.age == other.age

    def __ne__(self, other):
        return 'hello'
    def __gt__(self, other):  #> 会调用这个方法
        return  self.age  > other.age

    def __ge__(self, other): #>= 运算符的时候会调用
        return

    def __lt__(self, other): #使用< 会调用
        pass
    def __le__(self):  #<=
        pass

    def __add__(self, other): #+ 会调用
        return  self.age + other.age

    def __sub__(self, other):
        # return self.age - other
        return self.age - other.age

    def __mul__(self, other): #* 法
        pass

p1 = Person('zhangsan', 19)
p2 = Person('zhangsan', 18)

print(p1 is p2)
#== 运算符本质其实是调用对象的eq 方法，获取eq方法的返回结果
print(p1 == p2)

#!= 本质是调用__ne__方法，或者__eq__方法取反
print(p1 != p2)


print(p1 > p2)

#+ 法
print(p1 + p2)

#减法
# print(p1 - 9)
print(p1 - p2)

#str 将对象转换成字符串，会自动调用————str---方法
str() #打印对象也会调用
print(str(p1)) #转换成为字符串，默认会转换成为类型+内存地址
int() #调用对象的 int 方法

