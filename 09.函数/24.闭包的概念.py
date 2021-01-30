def outer():
    x = 10   #在外部函数里定义一个变量x，是一个局部变量
    def inner():
        nonlocal x #这里的x不再是新增的变量，而是外部的局部变量x
        y = x +1
        x = 20 # 不是修改外部的x变量，而是在inner函数内部又创建了一个新的变量
        print(y)
    return inner

outer()()