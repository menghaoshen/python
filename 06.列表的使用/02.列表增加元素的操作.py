# 列表是用来保存多个数据的
# 列表的操作，一般包括增删改查

heros = ['阿珂', '嬴政', '韩信', '露娜', '后裔', '亚瑟', '李元芳']

# 添加元素的方法 append insert extend

heros.append('黄忠')
print(heros)  # 在列表的后面追加一个数据

# insert(index,object) #需要两个参数
# index 表示下标，在哪个位置插入数据
# object 表示对象，具体插入哪个位置
heros.insert(3, '李白')
print(heros)

x = ['马可波罗','狄仁杰']
#extend(iterable) 需要一个可迭代对象
#a.extend(b) #将可迭代对象b添加到a里面，a变化，b不变
heros.extend(x) #需要一个可迭代对象
print(heros)
print(x)