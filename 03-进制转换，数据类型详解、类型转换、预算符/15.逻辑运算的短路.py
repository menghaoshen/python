#逻辑与运算，只有所有的运算符都是True，结果才是True
#只有有一个运算数是False，结果就是False
4 > 3 and print('hello')
4 < 3 and print('您好世界')

#逻辑或运算，只有所有的运算符都是False，结果测试False
#只要有一个运算符是True，结果就是True
4 > 3 or print('哈哈哈')
4 < 3 or print('嘿嘿')

#短路： 只要遇到False，就停止了，不在继续执行了
#逻辑运算的结果，不一定是布尔值
#逻辑与运算取值时，取得是第一个为False的值，如果所有的运算数都是True，取最后一个
print(3 and 5 and 0 and 'hello') # 0
print('good' and 'yes' and 'ok' and '100') #100

print(0 or [] or 'list' or 'ok') #list
print(0 or [] or {} or ()) #()