import  time
#计算代码运行时长的函数
def cal_time(fn,*args,**kwargs): #使用*args,**kwargs 可以传递多个参数
    print('我是外部函数，我被调用了')
    def inner(x):
        start = time.time()
        s = fn(x)
        end = time.time()
        print('代码运行花了{}秒'.format(end - start))
        return  s

    return  inner

@cal_time  #第一件事，调用cal_time  第二件事情，会把被装饰的函数传递给fn
def foo(n):
    x = 0
    for i in range(1,n):
        x += i
    return x

#统计foo运行时间
#再次调用foo的时候，这时的foo已经不是上面的foo了，是inner 函数
print('装饰后的foo={}'.format(foo))
m =  foo(1000)
print('m的值是',m)