#函数的三要素： 函数名，参数和返回值
#在python里面不允许函数重名，如果函数重名，后一个函数会覆盖前一个函数

def test(a,b):
    print('hello,a = {},b={}'.format(a,b))

def test(x):
    print('good ,x = {}'.format(x))

test(3)

# python 里面函数名，也可以理解为一个变量名
# 函数名不要使用系统内置的类和系统内置的函数
