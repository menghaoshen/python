# 在python里面，可以使用一对单引号和双引号，一对三引号和，一对三个单引号
a = 'hello'
b = "hello"
c = """hello"""
d = '''hello'''

# 如果字符串里面还有双引号，建议外面使用单引号
# 如果字符串里面有单引号，外面建议使用双引号
m = 'xiaoming said ：" I am xiaoming"'
n = "'I'm xiaoming"
c = """ xiaoming said :"xiaoming" """

# 字符串里面的转移字符 \
# \' ===> 显示一个普通的单引号
# \" ==> 显示一个普通的双引号
# \n ==> 表示一个换行
# \t===> 显示一个制表符
# \\ ===> 表示一个普通的反斜线

x = 'I\'m xiaoming'  # \ 表示的是转移字符，作用是对\后面的字符进行转移
y = 'I\"m xiaoming'  # \ 表示的是转移字符，作用是对\后面的字符进行转移
z = 'hello \n world'
print(z)

x1 = '您好\t 世界'
print(x1)

x2 = 'good mor\\ning'
print(x2)

# 在字符串前面加个r，在python里面表示的是原生的字符串
x3 = r'hello \teacher'
print(x3)
