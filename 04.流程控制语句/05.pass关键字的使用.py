#pass 关键字在python里面没有意义，只是单纯的用来占位，保证的语句的完整性

age = int(input('请输入您的年龄'))

if age >= 18:
    pass #使用pass用来占位，没有意义，为了保持语句的完整性，使程序不报错。
    print('欢迎来到我的网站')
print('hello')