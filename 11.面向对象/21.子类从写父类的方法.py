#继承的特点，如果一个类A，继承类B，由类A创建出来的实例对象都能直接使用类B里定义的方法

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sleep(self):
        print(self.name + '正在睡觉')

class Student(Person):
    def __init__(self,name,age,school):
        # self.name = name
        # self.age = age
        #子类在父类实现的基础上，又添加了自己新的功能
        #调用父类方法有两种方式
        #1. 父类名.方法名(self,参数列表)
        # Person.__init__(self,name,age)
        #2. 使用super 直接调用full的方法，推荐是第二种方法
        super(Student,self).__init__(name,age)
        self.school = school
        #

    def sleep(self):
        print(self.name + '正在课间休息时睡觉')
    def study(self):
        print(self.name + '正在睡觉')

s = Student('jerry',20,'大宝幼儿园') #调用父类的__init__方法
s.sleep() #调用父类的sleep 方法 #优先调用自己的的方法
print(Student.__mro__)

#1. 子类的实现和父类的实现完全不一样，子类可以选择重写父类的方法
#2. 子类在父类的继承上有更多的实现
