
import  threading
import  queue
import  time
#queue 结构可以在不同的线程间拆传递数据
def produce():
    for i in range(10):
        time.sleep(0.1)
        print('生产了++++面包b{}'.format(i))
        q.put('b{}'.format(i)) #消息放到队列里面

def consumer():
    for i in range(10):
        time.sleep(0.1)
        # q.get 是个阻塞的方法
        print('买到了-----面包{}'.format(q.get()))



q = queue.Queue() #创建了一个q
p1 = threading.Thread(target=produce,name='p1')
p2 = threading.Thread(target=consumer,name='p2')

p1.start()
p2.start()

#队列就是先进先出