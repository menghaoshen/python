# 进制转换 将int 类型以不同的形式表现出来
#类型转换  将一个类型的数据转换为其他类型的数据
# int ===》 str  str===》 int  bool ===》 int int====float

age = input('请输入您的年龄:')
#input 接收的用户输入都是str字符串类型
# python里面字符串和数字做加法运算，会直接报错
# 可以把字符串的变量age 转换成数字类型的age

print(type(age)) #str 字符串
#使用int 内置类可以将其他数据类型转换成整数
new_age = int(age)
print(type(new_age)) #int 数字
print("您明年%d " %(new_age + 1))