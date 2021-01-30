import re

#正则修饰符是对正则表达式进行修饰
#. 表示除了换行以外的字符
#re.S  让.匹配换行
x = re.search(r'm.*.a', 'sdfmoejo\nasd1',re.S)
print(x)

#re.I 忽略大小写
y = re.search(r'X','good Xyz',re.I)
print(y)

# \w 表示的是字母和数字 + 出现一次以上 $: 以指定的内容结尾

#re.M $能匹配到换行
z = re.findall(r'\w+$','i am boy\n you are girl\n he is man',re.M)
print(z)