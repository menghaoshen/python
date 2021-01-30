import  multiprocessing
import time
import  os
def dance(n):
    for i in range(n):
        time.sleep(0.5)
        print('正在跳舞，pid={}'.format(os.getpid()))
def sing(m):
    for i in range(m):
        time.sleep(0.5)
        print('正在唱歌,pid={}'.format(os.getpid()))

if __name__ == '__main__':
    print('主进程的PID:{}'.format(os.getpid())) #可以后期进程的pid
    # 创建两个进程
    # target 表示用来执行的任务
    #args 用来传参，类似是个元组
    p1 = multiprocessing.Process(target=dance,args=(20,))
    p2 = multiprocessing.Process(target=sing,args=(20,))

    p1.start()
    p2.start()
