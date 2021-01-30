person = {'name': 'zhangsan', 'age': 18, 'height': '180cm'}

# 特殊在列表和元组是但单一的数据，但是字典是键值对的形式

# 第一种的遍历方式
for x in person:
    print(x, '=', person[x])

# 第二种方法，获取所有的key，然后再遍历key，根据key获取value
for k in person.keys():
    print(k, '=', person[k])
# 第三种方式 获取所有的value
# 只能拿到值，不能拿到key 一般不用
for v in person.values():
    print(v)

# 第四中遍历的方式
for item in person.items():
    print(item[0], '=', item[1])

for k,v in person.items():
    print(k,'=',v)

#看到100集了