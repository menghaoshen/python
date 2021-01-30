# 字母表示它本身，很多字母前面加\会有特殊含义
# \n 表示换行
# \t 表示制表符
# \s 空白字符
# \S 非空白字符

import  re
# \d 表示数字，等价于[0-9],默认匹配一个数字，需要加个+ 匹配多个数字
print(re.search(r'x\d+p','x234p'))

# ^ 除了表示指定的内容以外，在[]里面可以表示取反
# \D 表示非数字，等价于[^0-9]
print(re.search(r'\D+','hell0'))
print(re.search(r'[^0-9]+','hell0'))

# \w 表示数字，字母以及_ 等价于[0-9a-zA-Z],一次或多次,非标点符号,中文也可以拿
print(re.findall(r'\w+', 'Hell0_9*._+=X0'))
print(re.findall(r'\w+', '大9*._+家=X0'))

# \W 非数字或者字母 和\w 取反
print(re.findall(r'\W+','大9*._+家=X0'))
