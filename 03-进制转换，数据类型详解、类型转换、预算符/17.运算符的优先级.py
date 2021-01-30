print(10 + 2 * 3 ** 2) #28

#逻辑运算的优先级 not > and > or
print(True or False and True) #True
print(False or not False) #True
print(True or True and False) #True

# 在开发中，使用括号来说明运算符的优先级
print(True or True and False)
print(True or (True and False))

