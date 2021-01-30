print(all(['hello', '1']))  # 把所有的元素都转换为布尔值，全是True 就是True
print(any(['hello', 0]))  # 有一个是True，就是True
# 转换相关
print(bin(7))  # 转换成二进制
print(chr(97))  # 将编码转换成字符
print(ord('a'))  # 将字符转换成编码

# 列出所有支持的方法
nums = [1, 2, 3]
print(dir(nums))

shang,yushu = divmod(8,3)
print(shang,yushu) #求商和余数

exit(0) #以指定的退出码，退出程序

#变量相关的
globals()  #查看所有的全局变量
locals() #查看局部变量

id #获取数据的内存地址

#输入输出
print() #打印内容
input() #让用户输入内容

#
len() #获取长度

#求最大数
max()
min() #求最小数

#打开一个文件
open()

#用来排序的
sorted()

#把数据变成字符串
repr()

