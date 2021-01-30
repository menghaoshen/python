# 多态是基于继承，通过子类重写父类的方法，
# 达到不同的子类对象调用相同父类的方法，得到不同的结果
# 提高代码的灵活度
class PoliceDog(object):
    def attack_enemy(self):
        print('警犬正在攻击坏人')

class BlindDog(object):
    def lead_road(self):
        print('导盲犬在领路')

class Person(object):
    def __init__(self,name,dog):
        self.name = name
        self.dog = dog # dog 指向的是PoliceDog
    def work_with_pd(self):
        print(self.name + '正在工作')
        self.dog.attack_enemy() #self.dog 相当于PoliceDog

    def work_with_bd(self):
        self.dog.lead_road()

#警察
# pd = PoliceDog()
# police = Person('张警官',pd)
# police.work_with_pd()


# bd = BlindDog()
# police = Person('张警官',bd)
# police.work_with_bd()


#需要把god 参数删除
# p = Person('zhangsan')
#
# bd = BlindDog()
# p.dog = bd
# p.work_with_bd()