a = 100  # 是全局变量，在py文件里面可以全局访问
world = 'hello'


def test():
    x = 'hello'  # 这个变量是函数内部定义的变量，它是局部变量，只能在函数内部使用
    print('x = {}'.format(x))

    # 如果局部变量的名和全部变量同名，函数内部又定义了一个新的局部变量
    # 而不是修改全局变量
    a = 10
    print('函数内部的a = {}'.format(a))

    # 函数内部修改全局变量
    # 使用global对变量进行声明，可以通过函数修改全局变量的值
    global world
    world = 'ok'
    #查看全局变量和局部变量
    print('locals = {},globals = {}'.format(locals(),globals()))


test()

print('函数外部的a = {}'.format(a))
print('函数外部的world={}'.format(world))

# 内置函数 global() locals() 可以查看局部变量和全局变量


#在python里面，只有函数能分割作用域
if 3 > 2:
    m = 'hi' #m是全局变量
print(m)