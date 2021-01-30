# 函数的返回值
# 返回值就是函数执行的结果，并不是所有的函数都必须有返回值
def add(a, b):
    c = a + b
    return c

# 获取add函数的结果，然后再求结果的4次方
result = add(1, 3)
print(result ** 4)