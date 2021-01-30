#with 语句后面的结果对象，需要重写，__enter__和exit方法
#当进入with代码块时，会自动调用__enter__方法里的代码
#当with代码块执行完成以后，会自动调用__exit__方法

class Demo(object):
    def __enter__(self):
        print('__enter__方法被执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def create_obj():
    return Demo()

with create_obj() as d: #as 变量名
    print(d)   #变量d 不是create_obj的返回结果
               #它是创建的对象x调用__enter__之后的返回结果
