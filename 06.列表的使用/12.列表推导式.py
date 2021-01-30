# 列表推导式作用是使用简单的语法创建一个列表
nums = [i for i in range(10)]
print(nums)

xx = [i for i in range(10) if i % 2 == 0]
print(xx)


points = [(x,y) for x in range(5,9) for y in range(10,20)]
print(points)
#请写出一段python代码，代码实现分组一个list里面的元素，比如[1,2,3,4,5...100]变成[[1,2,3][4,5,6]]
m = [i for i in range(1,101)]
print(m)
n = [m[j:j+3] for j in range(0,100,3)]
print(n)