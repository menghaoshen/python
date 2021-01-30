class Person(object):
    def __new__(cls, *args, **kwargs):
        return  object.__new__(cls)

    def __init__(self,name,age):
        self.name = name
        self.age = age



p = Person('zhangsan',18)
print(p)