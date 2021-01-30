class Student(object):
    __slots__ = ('name','age') #这个属性直接在定义在类里面，是一个元组，用来规定对象可以存在的属性
    def __init__(self,x,y):
        self.name = x
        self.age = y

    def say_hello(self):
        print('大家好我是',self.name)
#student('张三 '，18)
#1.调用__new__ 方法，申请一段内存空间
#2.调用__init__方法，并让self指向申请好的那段内存空间,填充数据
#3.变量s1 也指向创建好的内存空间
#3.变量s1 也指向创建好的内存空间
s1 = Student('张三 ',18)
s1.say_hello()
print('s1的名字是',s1.name)

s2 = Student('jack',19)
s2.say_hello()

# print(s1.height)  #没有属性会报错

#动态属性，可以动态添加，可以使用__slots__规定不能使用动态属性


# 直接使用等号给一个属性赋值
# 如果这个属性以前不存在，会给对象添加一个新属性
s1.city = '上海' #给对象添加一个city 属性
print(s1.city)
#如果这个属性以前存在，会修改这个属性对应的值
s1.name = 'jack'
print(s1.name)
