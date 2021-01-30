#python 里面的for 循环指的是for..in 循环。和C语言里面的for一样
#for 语言的格式： for ele in iterate

#range 内置的类用来生成区间的整数序列
#注意： in 的后面必须是一个可迭代的对象
# 目前接触的可迭代的对象，字符串，列表，字典，元组，集合，range
for i in range(0,10):
    print(i)

#列表
for x in [1,2,3,4,5,6,7,8,9,10]:
    print(x)

#字符串
for y in 'hello':
    print(y)

#计算1到100之和
z = 0 #定义一个变量，用来保持所有的数字的和
for j in range(1,101):
    z += j
print(z)
