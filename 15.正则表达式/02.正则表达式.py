# 用来处理字符串，对字符串进行检索和替换
# 1. 查找 2.替换
import re
x = 'hello\\nworld'
#在正则表达式里面，如果想匹配一个\，需要使用\\\\

#第一个参数就是正则匹配规则
#第二个参数是需要匹配的字符串
m =  re.search('\\\\',x) #mathch 和search
m =  re.search(r'\\',x) #mathch 和search
print(m)
# search 和mathc方法的执行结果是一个mathc类型的对象
