master = ['王昭君', '甄姬', '貂蝉', '妲己', '小乔', '大乔']

# 删除数据的三个方法 pop remove clear
# pop 方法默认会删除列表里最后一个数据，并返回这个数据
# pop 还可以传入index参数，可以用来删除指定位置上的数据

x = master.pop(3)  # ['王昭君', '甄姬', '貂蝉', '小乔', '大乔']
print(master)

# remove 用来删除指定的元素
master.remove('小乔')
# master.remove('妲己')  # 数据不存在，会报错
print(master)  # ['王昭君', '甄姬', '貂蝉', '大乔']

# del 也可删除数据
del master[2]
print(master)

# clear 用来清空一个列表
master.clear()
print(master)

tanks = ['亚瑟', '程咬金', '盾山', '张飞', '廉颇', '程咬金']
# 查询相关的方法
print(tanks.index('盾山'))  # 查看下标
# print(tanks.index('庄周')) # 元素不存在，就会报错
print(tanks.count('程咬金'))  # 计算次数
# in 运算符
print('亚瑟' in tanks)  # True

# 修改元素
# 使用下标可以直接修改列表里面的数据
tanks[5] = '恺'
print(tanks)
