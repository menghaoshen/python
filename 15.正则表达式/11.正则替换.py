# 正则表达式作用来对字符串进行检索和替换
# 检索 match search fullmatch finditer findall
# 替换 sub
import re

print(re.sub(r'\d', 'x', 'fasd08943928493sdfdsfds'))
print(re.sub(r'\d+', 'x', 'fasd08943928493sdfdsfds'))  # 多个数字替换成一个字母

p = 'hello34good23'  # 把字符串里面的数字*2 @hello68good46


# 第一个参数是正则表达式
# 第二个参数是新字符或者一个函数
# 第三个参数是需要被替换的原来的字符串
def test(x):
    y = int(x.group(0))
    y *= 2
    return str(y)


# sub 内部在调用test方法时，会把每一个匹配到的数据以，re.match的格式传参
print(re.sub(r'\d', test, p))  # test 自动调用的
