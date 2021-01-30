def foo(a, b):
    return a + b


x = foo(4, 5)  # 函数名，作用是调用函数，获取函数的执行结果，并赋值给变量x
print(x)

fn = foo  # 相当于取了一个别名
print(fn(1, 2))

# 除了使用def 关键字定义一个函数以外，我们还可以使用lambda 表达式定义一个函数

# 用来表达一个简单的函数，函数的调用次数很少，基本上就是调用一次
lambda a, b: a + b  # 匿名函数，
# 调用函数的两种方式
# 1.给它定义一个名字(很少使用)
# 2. 把这个函数当做参数传给给另个一个函数使用（使用场景比较多）
mu1 = lambda a, b: a + b
print(mu1(4, 5))


def cale(a, b, fn):
    return fn(a, b)


# def add(x,y):
#     return  x + y
#
# def minus(x,y):
#     return  x - y

# print(cale(3, 4,add)) #函数回调
# print(cale(3, 4,minus))

x3 = cale(1, 2, lambda x, y: x + y)
x4 = cale(19, 3, lambda x, y: x - y)
x5 = cale(2, 7, lambda x, y: x * y)
x6 = cale(12, 3, lambda  x, y: x / y)
print(x3,x4,x5,x6)
