# + 可以用来拼接字符串，元组，列表
print('hello' + 'world')
print(('godd', 'yes') + ('hi', 'ok'))
print([1, 2, 3] + [4, 5, 6])

# - 只能用户集合，求差集
print({1, 2, 3} - {3})

# *： 可以用于字符串列表，表示重复多次
# 字典和集合不能用，字典和不能重复，集合也是去重的
print('hello' * 3)
print([1, 2, 3] * 3)
print((1, 2, 3) * 3)

#  in成员运输符
print('a' in 'abc')
print(1 in [1, 2, 3])
print(4 in (6, 4, 5))

# in 用于字典是用来判断key是否存在
print('name' in {'name': 'zhansan'})

# 带下标的遍历
# enumerate 一般用于列表和元组
# nums = [19, 82, 39, 12, 34, 58]
nums = (19, 82, 39, 12, 34, 58)
#带下标的遍历
for i,x in enumerate(nums):
    print('第%d个数据是%d' %(i,x))

person = {'name':'zhansan','age':18,'height':'180cm'}

for k,v in enumerate(person):
    print(k,v)