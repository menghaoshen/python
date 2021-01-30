class Person(object):
    """
    这是个一个测试
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name +'正在吃饭')

p = Person('张三',18)
p.eat()
#内置的属性
#dir 把对象支持的属性和行为列出来
print(dir(p))
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'eat', 'name']
print(p.__dict__) #把对象属性转换成为一个字典
print(p.__dir__()) #等价于=dir(p)
print(p.__doc__) #拿到类的说明内容