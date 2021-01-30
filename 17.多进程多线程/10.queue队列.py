import  multiprocessing,queue
q1 = multiprocessing.Queue() #进程间通信
q2 = queue.Queue()  #线程间通信

# 创建队列时，可以指定最大长度，默认值时0，表示不限

q = multiprocessing.Queue(5) #只能放5个，超过就要阻塞了,无法放进去了，除非拿出来一个
q.put('hello')
q.put('hello')
# print(q.full()) #判断是否满了
q.put('hello')
# q.get()  队列里面取数据
q.put('hello')
q.put('hello')
# print(q.full()) #判断是否满了
# block = True： 表示阻塞，如果队列已经满了，就等待
# timeout 超时，等待多久以后程序会出错，单位是秒
# q.put('hi',block=True,timeout=20)

# q.put_nowait('how')  #等价于block=False 放不进去就崩

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
q.get(block=True,timeout=1)
q.get_nowait() #拿不到就崩