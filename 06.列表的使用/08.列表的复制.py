# python里面的数据都是保持在内存里面
# 数据有可变类型和不可变类型
# 不可变类型： 字符串，数字
# 可变类型：列表，字典，集合
# 不可变数据类型，如果修改值，内存地址会发生变化
# 可变数据类型，如果修改值，内存地址不会发生变化
# 使用id可以获取到内存的地址


# a = 12
# b = a
# print('修改前a = {},b = {}'.format(id(a), id(b)))
# a = 10
# print(b)
# print('修改后a = {},b = {}'.format(id(a), id(b)))
#
# nums1 = [100, 200, 300]
# nums2 = nums1
# print('修改前的id num1 = {},num2={}'.format(id(nums1), id(nums2)))
# nums1[0] = 1
# print(nums2)
# print('修改后的id num1 = {},num2={}'.format(id(nums1), id(nums2)))

# 列表的复制
x = [100, 200, 300]
y = x  # x 和 y 指向了同一个内存空间，会相互影响 ，等号是内存地址的复制
z = x.copy() # 调用copy方法，可以复制一个列表，这列表和原有的列表内容一样，但是指向不同的内存空间
x[0] = 1
print(y)

print('x的内存地址%x，y的内存地址%x,z的地址空间%x'%(id(x),id(y),id(z)))
print(z)

#除了使用列表自带的copy方法以外，还可以使用copy模块实现拷贝
import copy
a = copy.copy(x) #效果等价于x.copy() 都是浅拷贝

#切片其实就是一个浅拷贝
names1 = ['张三','李四','王五','杰克']
names2 = names1[::]
names1[0] = 'jerry'
print(names2)
#看到85