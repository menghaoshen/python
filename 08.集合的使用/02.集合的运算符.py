first = {'李白','白居易','李清照','杜甫','王昌玲','孟浩然','王安石'}
second = {'李商隐','杜甫','李白','白居易','王昌龄','岑参'}
third = {'李清照','刘禹锡','岑参','王昌玲','苏轼','王维','李白'}

#set 支持很多算法，不支持加号 +

print(first - second)  # a -b 求a和b的差集
print(first & second) # a & b 和的交集 a和b都有的
print(first | second) # a | b 求a和b的并集，
print(first ^ second) # a ^ b 差集的并集 ，要不同的，相同的就不要

