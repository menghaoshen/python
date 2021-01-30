a = 13
b = 20

# 方法一，使用第三方变量
# c = b
# b = a
# a = c
# print(a)
# print(b)
# 方法二，使用运算符
# a = a + b
# b = a - b
# a = a - b
# print(a)
# print(b)

# 方法三，使用异或运算符
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a)
# print(b)

# 方法四，使用pytohn独有的
a, b = b, a
print(a)
print(b)
