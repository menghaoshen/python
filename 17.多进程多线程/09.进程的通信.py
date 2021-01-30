import  os
import  multiprocessing
import time

def create(x):
    for i in range(10):
        print('生产了++++++pid{} {}'.format(os.getpid(),i))
        x.put('pid{} {}'.format(os.getpid(),i))

def consumer(x):
    for i in range(10):
        print('消费了------{}'.format(x.get()))

if __name__ == '__main__':
    q = multiprocessing.Queue()
    c1 = multiprocessing.Process(target=create,args=(q,))
    c1.start()
    c2 = multiprocessing.Process(target=consumer,args=(q,))
    c2.start()