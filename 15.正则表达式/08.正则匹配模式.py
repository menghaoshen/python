import re

# \s 表示任意的非打印字符，空白字符串
x = 'hello world'
print(re.search(r'\s', 'hello world'))  # 空格
print(re.search(r'\s', 'hello\nworld'))  # 换行
print(re.search(r'\s', 'hello\tworld'))  # 制表符

# \S 表示非空白字符
print(re.search(r'\S', '\t\n x'))

# 标点符号的使用
# () 就是一个分组
m = re.search(r'h(\d+)x', 'dh876xkflas')  # () 829
print(m.group(1))
#如果要表示括号，要使用\斜杠
m1 = re.search(r'\(.*\)', '(1+1)*3+5')
print(m1.group())

# .表示除了换行以外的的任意字符。如果想要匹配 . 需要使用\


# [] 用来表示可选项范围 [x-y] 从x到y区间，包含x和y
print(re.search(r'[0-5]', 'pdfs6m'))  #匹配0-5的数字
print(re.search(r'[0-5]+', 'pdfs6887m'))  #匹配多个数字
print(re.search(r'[0-5a-d]+', 'pdfs1fdm'))  #

# | 用来表示或者 和中括号有一定的相识，但是有区别
# [] 的值表示的是区间， | 是可选值
print(re.search(r'f(x|p|t)m', 'pdsfxm'))

# {} 用来限定出现的次数
# {}：表示前面的元素出现n次
# {n,} :表示前面的元素出现n次以上
# {,n} : 表示前面的元素出现n次一下
print(re.search(r'go{,2}d','good'))
#{m,n}: 表示前面的元素出现m到n次
print(re.search(r'go{3,5}d','goooooood'))

# * 表示前面的元素出现任意次数(0次及以上)，等价于 {0,}
print(re.search(r'go*d','gooood'))

# + 表示前面的元素至少出现一次，等价于{1,.}
print(re.search(r'go+d', 'goood'))

# ? 两种用法，1 规定前面的元素，最多只能出现一次，等价{,1}
# 2. 将贪婪模式转换成非贪婪模式
print(re.search(r'go?d','goood'))

#^ 以指定的内容开头，$指定内容结尾
print(re.search(r'^a.*i$','akjlji'))