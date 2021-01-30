person = {'name': 'zhangsan', 'age': 18,'addr':'zmd'}
print(person['name'])

# 直接使用key可以修改对应的value
# 如果key存在，会修改vlues
# 如果不存在，会添加一个新的的vlues
person['name'] = 'list'
person['gender'] = 'female'
print(person)

# 把name对应的键值对删除,执行结果是被删除的value
person.pop('name') #
print(person)
# popitem   删除一个元素，结果是被删除的这个元素组成的键值对
result = person.popitem()
print(result)
print(person)
#del 也可以删除
del person['addr']
print(person)
#清空一个字典
person.clear()
print(person)