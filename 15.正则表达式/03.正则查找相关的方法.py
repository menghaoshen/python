# 查找相关的方法
# match： 和 search:
# 共同点： 1.只对字符串查询一次，2.返回值类型都是re.Match 类型的对象
#不同点： match 是从头开始匹配，一旦匹配失败，就返回None，search是在整个字符串里面找
# finditer： 查找所有的匹配数据，放到一个可迭代对象里
# findall 把查找到的所有字符串结果，放到一个列表里面
# fullmatch 完整匹配，字符串需要完全满足正则规则才会有结果，否则就是None
import  re
from collections.abc import Iterable

m1 = re.match(r'good','hello wrold good morining')
print(m1)

m2 = re.search(r'hello','hello wrold good morining hello')
print(m2)

#finditer 返回的是一个可迭代对象
m3 = re.finditer(r'x','fdafdafaxxfdaxx')
print(isinstance(m3,Iterable))
print(m3)
for i in m3:
    print(i)

m4 = re.findall(r'x\d+','fdafdafax1xfdax2xdfdxx')
print(m4)

m5 = re.fullmatch(r'h.*d','hello world')
print(m5)