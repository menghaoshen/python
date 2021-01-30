# - 小明今年18岁.身高1.75，每天早上跑完步，回去吃东西
# - 小美今年17岁，身高1.65，小美不跑步，小美喜欢吃东西

# 定义类：类名怎么定义，使用class 来定义一个类
# class 类名，类名一般需要遵守大驼峰命名法，每一个单词的首字母都要大写
# class 类名：
# class 类名(object):

class Student(object):  # 关注这个类,有哪些属性和行为
    def __init__(self, name, age, height):  # 在 init 方法里，以参数的形式定义属性
        self.name = name
        self.age = age
        self.height = height

    #行为定义为一个个的函数
    def run(self):
        print('正在跑步')

    def eat(self):
        print('正在吃东西')

#Stundet() 会自动调用__int__方法
#使用student 类，创建两个实例对象s1 ，s2
#s1 s2 都有name，age，height 的属性，同时又run和eat方法
s1 = Student('小明',19,180)
s2 = Student('小美丽',18,165)
#根据业务逻辑，让不同的对象执行不同的行为

s1.run()
s2.run()
s2.eat()