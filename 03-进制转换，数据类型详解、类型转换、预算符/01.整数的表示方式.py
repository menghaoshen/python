#python 里面的数据类型：
# 整形（int） 浮点型（float） 复数（complex） 字符串（str） 布尔（bool）
# 列表（list） 元组（tuple） 字典（dict） 集合（set）

# 整型就是整数，计算机其实只能保持二进制 0 和 1，为例方便数据的表示，同时计算机也支出八进制和十六进制
# 二进制， 八进制 十六进制 十进制 在python里面都能表示
a = 98  #默认数字都是十进制的数字， 98 是就是十进制的九十八
b = 0b101101101 #在python里面以ob开头的是二进制
print(b) #用print语句打印的时候默认是十进制打印的
# 二进制里面最大的个位数是1，不能出现2
c = 0o34 #以0o开头的数字是八进制的数字
print(c) #28

d = 0x23  #以0x开头的数字是十六进制
print(d)  #23
#十六进制分别是
# 0、1、2、3、4、5、6、7、8、9、A、B、C、D、E、F