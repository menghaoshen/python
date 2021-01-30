def outer(x):
    m = 100
    print('我是outer函数')
    def inner():
        print('我是inner函数')
    if x > 18:
        inner()
    return 'hello'
outer(21)