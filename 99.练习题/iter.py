list=[1,2,3,4]
it = iter(list) #创建迭代器对象
for x in it:
    print(x,end=" ")

#使用next() 函数
import sys
list = [1,2,3,4]
it = iter(list)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()