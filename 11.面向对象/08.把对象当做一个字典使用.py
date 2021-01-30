class Person(object):
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    def __setitem__(self, key, value): #key = 张三
        # print('setitem方法被调用了,key={},value={}'.format(key,value))
        P.__dict__[key] = value
P = Person('张三',18,'北京')
print(P.__dict__) #将对象转换为字典 {'name': '张三', 'age': 18, 'city': '北京'}
#不能直接把一个对象当做字典来使用
P['name'] = 'jack' #[] 语法会调用对象的_setitem_方法
P['age'] = 20
print(P.name)
print(P.age)