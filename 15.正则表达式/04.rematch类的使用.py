#调用re.match，re.search 或者对re.finditer结果进行遍历
#拿到的内容都是re.match类型对象
# .任意字符
# *出现的次数

import  re
m = re.search(r'm.*a','orjomjadas')
# print(dir(m))
print(m.span()) #匹配到的结果字符串的开始和结束下标,默认的是第0组的开始和下标

#使用group方法可以获取匹配的字符串结果
#group 可以穿参，表示第n个分组
print(m.group(0)) #获取匹配的字符串结果

#group 方式表示正则表达式的分组
# 1. 在正则表达式里面使用（）表示一个分组
# 2. 如果没有分组，默认只有一组
# 3. 分组的下表从0开始
m1 = re.search(r'(9.*)(0.*)(5.*7)','da9fi0riel5kfsda7ifsdaiferit')  #使用()分组 #一共4组，0是整个，1组是9.* 2组是0.*
print(m1.group()) #默认就是第0组
print(m1.group(1)) #默认就是第0组
print(m1.group(2)) #默认就是第0组
print(m1.groups()) #('9fi', '0riel', '5kfsda7')
#groupdict 作用是获取到分组组成的字典
#(?P<name>表达式) 可以给分组起一个名字
m2 = re.search(r'(9.*)(?P<name>0.*)(5.*7)','da9fi0riel5kfsda7ifsdaiferit')  #使用()分组 #一共4组，0是整个，1组是9.* 2组是0.*

print(m2.groupdict()) #{'name': '0riel'}
print(m2.groupdict('name'))#{'name': '0riel'}
