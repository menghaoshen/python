#大于> 小于> 大于等于>= 小于等于<= 不等于!= 等等与==
print(2 > 1)
print(2 < 4)
print(4 >= 3)
print(5 <= 6)
print(5 != 6)
# print(5 <> 6) python3 里面不支持<> 2支持

print('hello' == 'hello')

#比较运算符在字符串里面的使用
#字符串之间使用比较运算符，会根据各个字符的编码逐一进行比较
print('a' > 'b') #False 97 > 98
print('abc' > 'b') #False 97 > 98

#数字和字符串之间，做==运算的结果是False，做！=结果是True 不支持其他的比较运算
print('a' == 90)
print('a' != 97)
