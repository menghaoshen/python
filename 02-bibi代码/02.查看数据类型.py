a = 34
b = 'hello'
c = True
d = ['张三','李四']

# 使用type 内置类可以查看一个变量对应的数据类型
print(type(a)) # <class 'int'> 整数
print(type(b)) # <class 'str'> 字符串类型
print(type(c)) # <class 'bool'> 布尔类型
print(type(d)) # class 'list'> 列表
print(type(3.14)) #<class 'float'> 浮点类型

#在python里面，变量是没有数据类型的，我们所说变量的数据类型，其实是变量对应的值得数据类型
x = 23
print(type(x)) #<class int>
x = 'hello'
print(type(x)) #<class str>