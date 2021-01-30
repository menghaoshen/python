#元组和列表很像，都可以用来保存多个数据
#使用一对小括号（），来表示一个元组
#元组和列表的区别在于，列表是可变的，而元组是不可变的数据类型

words = ['hello','yes','good'] #列表，使用[]
nums = (12,2,3,4,5,6,9,9,9) #元组，使用() 表示

#和列表医院，也是一个有序的数据存储的容器
#可以通过下标来获取元素
print(nums[2])
print(nums.index(3)) # 通过数字获取下标
print(nums.count(9)) #统计9出现的次数

#特殊情况，如何表示只有一个元素的元组
age = (18)  #这个种书写方式是个整数，不是一个元组
age = (18,)  #这样写是一个元组
print(type(age))

#tuple 内置类
# print(tuple(18)) #报错
print(tuple('hello')) #('h', 'e', 'l', 'l', 'o')

#把列表转换层元组，元组转换成列表
print(tuple(words)) # tuple list set 都是这样使用的
print(list(nums))  #转换成列表

#join 连接字符串,把元组恢复成字符串
print(''.join(('h', 'e', 'I', 'I', 'o')))

#元组也可以便利
for i in nums:
    print(i)

j = 0
while j < len(nums):
    print(nums[j])
    j += 1
