# 集合是一个不重复的无序的集合，可以使用{} 或者set 来表示
# {} 有两种意识，字典使用大括号，集合也是大括号
#{} 如果里面放的是键值对就是字典，如果{}里面放的是单个的值，就是一个集合
person ={'name':'zhangsan','age':18} #字典
x = {'hello',1,'good'}

#如果有重复的数据，，会自动去重
names = {'zhangsan','lisi','jack','tony','jack','lisi'}
print(names)

#set 可以增删改查
names.add('马云') #添加一个元素
print(names)

names.pop()  #删除一个元素，随机删除了
names.remove('jack') #删除一个指定的元素，如果没有就会报错
print(names.union('刘能', '赵四')) #将多个集合合并成一个新的集合
names.update('刘能','赵四') #a.update(b) 将b拼接到a里面
print(names)
names.clear() #清空一个集合
print(names)  #空集合的表现方式是set() 不是{} {} 是字典

print('jack' in names)  #可以用in的方法