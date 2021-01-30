import time
class Fibonacci(object):
    def __init__(self,n):
        self.n = n
        self.num1 = self.num2 = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.n:
            x = self.num1
            self.num1,self.num2 = self.num2,self.num1 + self.num2
            # time.sleep(1)
            return x
        else:
            raise  StopIteration

# 1，2,3,4,5,13,21,34,55,89,144
f = Fibonacci(5) #占用时间，不占空间
for i in f:
    print(i)


#既然有列表，为啥还有生成器,节省内存，
nums = [1,2,3,4,5,13,21,34,55,89,144,233,377,] #站空间，不占时间