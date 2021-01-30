# split splitlines partition rpartition

x = 'zhangsan，lisi，wangwu，jerry，henry，merry，jack，tony'
# ['zhangsan，lisi，wangwu，jerry，henry，merry，jack，tony']
# 使用split 方法，可以讲一个字符串切割成一个列表
# y = x.split('，')
# print(y)
# print(x)
# z = x.rsplit('，',2)
# print(z)

# partition 指定一个字符串作为分隔符，分为三部分
# 前面，分隔符，后面
print('abcdefXXmpqrst'.partition('X'))  # ('abcdef', 'X', 'mpqrst')
print('abcdefXXmpqrst'.rpartition('X'))  # ('abcdefX', 'X', 'mpqrst')

# 获取文件名和后缀名

file_name = '2020.12.14不要打开.mp4'
print((file_name).rpartition('.'))
