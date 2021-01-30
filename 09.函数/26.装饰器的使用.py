import  time
#计算代码运行时长的函数
def cal_time(fn):
    print('我是外部函数，我被调用了')
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print('代码运行花了{}秒'.format(end - start))
    return  inner

@cal_time  #第一件事，调用cal_time  第二件事情，会把被装饰的函数传递给fn
def foo():
    print('hello')
    time.sleep(10)
    print('workd')

#统计foo运行时间
#再次调用foo的时候，这时的foo已经不是上面的foo了，是inner 函数
print('装饰后的foo={}'.format(foo))

