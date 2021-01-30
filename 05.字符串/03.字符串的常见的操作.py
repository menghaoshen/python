x = 'abcdefghijklmnl'

# 使用内置函数len获取字符串的长度
print(len(x))

# 查找相关的方法 find/index/rfind/rindex

print(x.find('l'))  # 可以获取指定字符的下标
print(x.index('l'))
# print(x.find('p')) #-1 如果字符在字符串里面不存在，结果是-1
# print(x.index(P)) # 使用inex。如果字符不存在，就报错

# 找最大的的索引
print(x.rfind('l'))
print(x.rindex('l'))

# is 开头的是判断，结果是布尔类型
print('hello'.startswith('he'))  # 是不是以he开头
print('hello'.endswith('o'))  # 是不是o结尾
print('hello12'.isalpha())  # 是不是字母
print('123'.isdigit())  # 是否是个数字，只能识别整数，小数不识别
print('123.12'.isdigit())  # 是否是个数字，只能识别整数，小数不识别

# alnum 判读是否由数字和在字母组成
print('abc123'.isalnum())  # True
print('123'.isalnum())  # True
print('abc'.isalnum())  # True
print('1 - b'.isalnum())  # False

print(' 1  '.isspace())  # 是否由空格组成
# 判读用户输入的是否是数字
# num = input('请输入一个数字')
# if num.isdigit():
#     num = int(num)
# else:
#     print('请输入数字')


# count 返回str 在star和end 之间在mystr出现的次数
# s.count(sub[,start,[,end]]) --int
mystr = '12345643'
print(mystr.count('-1'))

# 字符串的替换
# replace 方法
x = 'hello'
m = x.replace('l', 'x')  # raplace 将字符串里面的l替换成x
print(x)  # 字符串是不可变的数据类型
print(m)  # 原来的字符串不会改变，而是生成一个新的字符串来保存替换后的结果

# 修改大小写 capitalize
print('hello world\n yes'.capitalize())  # Hello world 首字母大写

# upper
print('hello'.upper())  # 全部大写
# lower 全小写
print('WoRLD'.lower())
# titile 每个单词的首字母大写
print('good morning'.title())
# 使用的地方
# while True:
#     content = input('请输入内容,输入exit退出')
#     print('您输入的内容是:', content)
#     if content.lower() == 'exit': #转成小写
#     # if content.upper() == 'EXIT': #转成大写
#         break

# ljust 让字符串以指定的长度显示,如果长度不够,默认在右边使用空格补齐
print('hello'.ljust(10, '+'))  # 要占10个字符的长度,
print('hello'.rjust(10))  # 左侧加空格加
# 单词居中.两边加空格
print('apple'.center(15, '*'))
# 去掉左边的空格
print('    pear     '.rstrip())
# 去掉两边的空格
print('    banana     '.strip())

# 以某种固定的格式显示的字符串,我们可以将它切割成为一个列表
x = 'zhangsan+lisi+wanwu+jack+tony+henry+chris'
names = x.split('+')
print(names)
# 讲列表转换成为字符串
fruits = ['apple', 'pear', 'peach', 'banan', 'orange', 'grape']
print('-'.join(fruits))  # join 后面是个可迭代对象
print('+'.join(('yes', 'ok')))

# 字符串的运算符
# 1. 字符串和字符串之间能够使用加法运算符，作用是将两个字符串拼接成为一个字符串串。例 如: 'hello' + 'world' 的结果是 'helloworld'
# 2. 字符串和数字之间可以做乘法运算，结果是将指定的字符串重复多次。例如: 'hello'*2 的结果 是 hellohello
# 3. 字符串和字符串之间，如果使用比较运算符进行计算，会获取字符对应的编码，然后进行比较。
# 4. 除上述几种运算符以外，字符串默认不⽀持其他运算符。



print('hello' + 'world')
print('hello' * 3)