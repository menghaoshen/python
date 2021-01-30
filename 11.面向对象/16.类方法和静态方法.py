class Person(object):
    type = 'human'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #这个方法需要打印对象的姓名
    def demo(self):
        print('姓名是',self.name)
    #这个方法只需要打印hello world

    #这样写不安全，不要这样写,因为实例名字，会经常变化
    # @ staticmethod
    # def foo():
    #     print(p.name)
    @staticmethod
    def foo():
        print(Person.type)

    @classmethod
    def bar(cls):
        print(cls.type)
p = Person('zhangsan',18)
# Person.foo()
p.demo()  #实例对象调用实例方法的时候，会自动将实例对象传递给self
Person.demo(p)

#静态方法，类方法，都可以通过类方法和实例方法调用
Person.foo()
p.foo()

Person.bar()