# 使用int 内置类可以将数据转换成为整数

a = '31'
b = int(a)
print(a)
print(b)

# print(a + 1) #报错
print(b + 1) #32

#如果字符串不是一个合法的数字，会直接报错
# x = 'hello'
# y = int(x)
# print(y)

x = '1a2c' #把字符串1a2c，当做十六进制转换成整数
y = int(x,16) #6700，默认是十进制输出
print(y)
print(bin(y)) #二进制打印

m = '12'
n = int(m,8) #把字符串的12 当做八进制转换成整数
print(n)