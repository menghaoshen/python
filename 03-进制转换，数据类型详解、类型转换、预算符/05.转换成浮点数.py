a = '12.34'
#使用内置float类可以将其他类型数据类型转换成float 浮点数
b = float(a)
print(b + 1)

#如果字符串不能被转换成有效的浮点数，就会报错
# c = float('hello')
# print(c)

c = 101
print(float(c))