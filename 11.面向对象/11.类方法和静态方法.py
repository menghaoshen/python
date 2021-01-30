class Person(object):
    type = 'human'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #实例方法,会用到实例对象属性,self指向调用这个方法的实例对象
    #两种调用方式:
    #实例对象,方法名,不需要手动给self传参,会自动将实例对象传递给self
    #类对象,方法名  需要手动给self传参
    def eat(self, food):  # 对象方法有一个self,指的是实例对象
        print(self.name + '正在吃东西' + food)

    # 如果一个方法里面没有用到实例对象的任何属性,可以将这个方法定义成静态方法

    @staticmethod  # 不用实例对象的任何属性
    def demo():  # 默认的方法都是对象方法
        print('hello')

# 如果这个函数只用到类属性,我们可以把它定义成为一个类方法
    @classmethod
    def test(cls):
        # 类方法有一个参数cls,也不需要手动传参,会自动传参
        # cls 指的是类对象,cls == person
        print(cls.type)
        print('yes')

p1 = Person('张三', '18')
# 实例对象在调用方法时,不需要给形参self传参,会自动的把实例对象传递给self

# eat 对象方法,可以直接使用实例对象,方法名(参数)调用
p1.eat('红烧牛肉泡面')  # 直接使用实例对象调用方法
p2 = Person('李四', '19')
p2.eat('momo')
print(p1 is p2)

# 对象方法还可以使用,类对象来调用类名.方法名()
# 这种方法,不会给self传参,需要手动的指定self
print(Person.eat(p2, '西红柿'))

# 静态方法的调用,没有用到实例对象的任何属性
Person.demo()
p1.demo()
#类方法,可以使用实例对象和类对象调用
p1.test()
Person.test()




# 静态的方法,没有用到实例对象的东西
class Utils(object):
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return  a - b


print(Utils.add(4, 5))
