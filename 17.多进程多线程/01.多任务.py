import  threading
import  time
def dance():
    for i in range(50):
        time.sleep(0.2)
        print('我正在跳舞')

def singe():
    for i in range(50):
        time.sleep(0.2)
        print('我正在唱歌')

dance()
singe()

# 多个任务同时执行
# python里执行多任务，多进程，多线程，多进程+多进程

#target 需要的是一个函数，用来指定线程需要执行的任务
t1 = threading.Thread(target=dance) #创建了线程1
t2 = threading.Thread(target=singe) #创建了线程2

# 启动线程
t1.start()
t2.start()