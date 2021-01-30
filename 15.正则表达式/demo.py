class Person(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name + '正在吃' + food)

    def sleep(self):
        print(self.name + '正在睡觉')

p = Person('张三')
# p.eat('西红柿鸡蛋')

eat = p.eat  #给对象的eat方法设置一个别名eat，不能加括号
#函数名后面如果加括号表示的是调用这个函数，并获取到函数的结果
# 不加括号表示函数的别名
