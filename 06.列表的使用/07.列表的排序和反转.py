nums = [6, 5, 3, 1, 7, 7, 2, 4]

# 调用列表的sort方法可以直接对列表进行排序
nums.sort() #默认是正序
nums.sort(reverse=True) #倒序
print(nums)

#不会改变原有的列表数据，会生产新的一个有序的数据
x = sorted( nums) #内置函数sorted
print(x)

#列表反转
name = ['zhangsan','lisi','wangwu']
name.reverse()
print(name)
print(name[::-1]) #切片的方法反转