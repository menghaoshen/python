import time
import threading

# 多线程可以同时操作以全局变量(多线程共享全局变量)
#线程安全问题
ticket = 20

#创建一把锁
lock = threading.Lock()

def sell_ticket():  
    global ticket
    while True:
        lock.acquire() #加同步锁
        if ticket > 0:
            time.sleep(0.1)
            ticket -= 1
            lock.release()
            print('{}卖出一张票，还剩{}张'.format(threading.current_thread().name, ticket))
        else:
            lock.release()
            print('票卖完了')
            break



t1 = threading.Thread(target=sell_ticket, name='线程1')
t2 = threading.Thread(target=sell_ticket, name='线程2')

t1.start()
t2.start()
