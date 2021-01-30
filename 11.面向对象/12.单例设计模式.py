class Person(object):
    _instance = None
    _is_first = True

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            #申请内存,创建一个对象,并把对象的类型设置为cls
            cls._instance = object.__new__(cls) #
        return cls._instance

    def __init__(self, a, b):
        if self._is_first:  #第一次会修改了,第二次就不会修改了
            self.a = a
            self.b = b
            self._is_first = False

s1 = Person('哈哈','嘻嘻')
s2 = Person('哈哈','喜喜')

#1. 调用__new__方法申请内存
#2. 如果不重写__new__方法,会调用object的__new__方法
#objict 的__new__方法会申请内存
#如果重新了__new__方法,需要自己手动申请内存
print(s1 is s2)
print(s1.a,s2.a)
print(s2.b,s2.b)
