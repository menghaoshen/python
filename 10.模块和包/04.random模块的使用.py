import  random
#用来生产a,b的随机整数
#包括开始和结束
print(random.randint(1, 2))

print(random.random()) #用来生成0,1的区间，包含0不包含1

#包含包含开始，不含结尾
print(random.randrange(1,2)) #用来生成a，b的数据整数

#choice #用来在可迭代对象里面，随机抽取一个数据
print(random.choice(['zhansn', 'lisi', 'jack', 'jerry']))

#sample 用来在可迭代对象里面随机抽取n个数据
print(random.sample(['zhansn', 'lisi', 'jack', 'jerry'], 2))