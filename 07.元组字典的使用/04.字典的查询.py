person = {'name':'zhangsan','age':18}

#查找数据（字典的数据在保存时，是无序的，不能通过下标来获取）
#不能通过value 找到key
print(person['name']) #通过key，获取对于的value
x = 'age'
print(person[x])

# print(person['height'])  #不存在，会报错
#获取一个key不存在，不报错，使用默认的值 返回none
print(person.get('height'))
print(person.get('gender','female')) #如果根据key获取不到value，使用给定的默认值
print(person)