import  time  #time 模块获取当前的时间

# #代码运行前，获取时间
# start = time.time() #time 模块里面的time 方法，可以获取当前时间的时间戳
# #时间戳是1970-01-01,00:00:00 UTC 到现在的秒数
# print(start)
# x = 1
# for i in range(1,200000):
#     x *= i
#
# print(x)
# end = time.time()
# print('代码运行花了{}秒'.format(end - start))
#代码运行完以后，在获取一下时间

# start = time.time()
# print('hello')
# time.sleep(1)
# print('world')
# end = time.time()
# print('代码运行花了{}秒'.format(end - start))


#计算代码运行时长的函数
def cal_time(fn):
    start = time.time()
    fn()
    end = time.time()
    print('代码运行花了{}秒'.format(end - start))

def foo():
    print('hello')
    time.sleep(10)
    print('workd')

#统计foo运行时间
cal_time(foo)