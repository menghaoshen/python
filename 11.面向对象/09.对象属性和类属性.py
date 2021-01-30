class person(object):
    type = '人类'  # 类里面，函数外面，是类属性
    def __init__(self,name,age):
        self.name = name
        self.age = age

# 对象P是通过Person 类创建处理的实力对象
# person 也是在内存里面存储着，person 是类对象，
# name 和 age 是对象的属性，每个实力对象都会单独保存一份的属性
# 每个实力对象之间的属性没有关联，互不影响
p1 = person('张三',18)
p2 = person('李四',20)

x  = p1
print(x.name)

#类属性可以通过类对象和实例对象获取
print(person.type) #可以通过类对象获取类属性
print(p1.type) #可以通过实例对象获取类属性


#类对象只能通过类对象来修改，无法通过实例对象修改
p1.type = 'human' #并不会修改类属性，而是给实例对象添加一个新的对象属性
print(p1.type)
#类的属性改了，实例的对象属性也会修改
person.type = 'human'
print(person.type)


