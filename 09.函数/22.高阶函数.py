# 1. 一个函数作为另一个函数的返回值
# 2. 一个函数作为另一个函数的参数
# 3. 函数内部在定义一个函数

def foo():
    print('我是foo，我被调用了')
    return  'foo'

def bar():
    print('我是bar，我被调用了')
    return foo

x = bar()
print('x的值是{}'.format(x))
print('----------')
y = bar()()
print(y)

def outer():
    m = 100
    def inner(): #内部函数，只能内部调用
        n = 90
        print('我是inner函数')
    print('我是outer函数')
    return  inner
outer()  #inner 函数不会被调用
outer()()  #调用函数内部的函数
