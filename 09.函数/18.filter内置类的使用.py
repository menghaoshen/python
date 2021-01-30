# filter 对可迭代对象进行过滤，得到的是一个filter 对象
# python2 的时候是一个内置函数，python3修改成了一个内置类

ages = [12, 23, 30, 17, 16, 22, 19]
#filter 可以给定两个参数，第一个参数是函数，第二个参数是可迭代对象
#filter 结果是一个filter类型得对象,filter 对象也是一个可迭代的对象
x = filter(lambda ele:ele > 18,ages)
# print(x) #<filter object at 0x000001810845D608>
# for a in x:
#     print(a)

adult = list(x)
print(adult)
