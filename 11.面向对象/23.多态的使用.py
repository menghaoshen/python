# 多态是基于继承，通过子类重写父类的方法，
# 达到不同的子类对象调用相同父类的方法，得到不同的结果
# 提高代码的灵活度
class Dog(object):
    def work(self):
        print('狗正在工作')


class PoliceDog(Dog):
    def work(self):
        print('警犬正在攻击坏人')

class BlindDog(Dog):
    def work(self):
        print('导盲犬在领路')

class DrugBog(Dog):
    def work(self):
        print('缉毒犬在找毒品')

class Person(object):
    def __init__(self,name):
        self.name = name
        self.dog = None
    def work_with_dog(self):
        if self.dog is not None and isinstance(self.dog,Dog):
            self.dog.work()

p = Person('zhangsan')

bd = BlindDog()
p.dog = bd
p.work_with_dog()

bd = PoliceDog()
p.dog = bd
p.work_with_dog()

bd = DrugBog()
p.dog = bd
p.work_with_dog()