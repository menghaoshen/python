#等号连接的变量可以传递赋值
a = b = c = d = 'hello'
print(a,b,c,d)

m,n = 3,5
print(m,n)
x = 'helo','good','yes' #元组
print(x)

#拆包时，变量的个数和值得数量不一致，会报错
# y,z = 1,2,3,4 #
# o,p,q = 4,2

*o,p,q = 1,2,3,4,5,6
print(o,p,q)#[1, 2, 3, 4] 5 6