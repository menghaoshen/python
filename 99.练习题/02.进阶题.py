#使用循环计算出1到100的和
# i = 0
# j = 0
# while i < 100:
#     i += 1
#     j += i
# print(j)
# r = 0
# for i in range(1,101):
#     r += i
# print(r)

# 统计1到100内个位数是2并且能够被3整除的数的个数
# count = 0 #计数器
# for i in range(1,100):
#     if i % 10 == 2 and i % 3 == 0:
#         count += 1
#         print(i)
#
# print('满足条件的个数是',count,'个')

#输入一个正整数，求他是几位数：
# num = int(input('请输入一个整数：'))
# count = 0
# while True:
#     count += 1
#     num //= 10
#     if num == 0:
#         break
# print('您输入的数字是'count)
#另一种写法
#打印所有的水仙花数
#水仙花是一个三位数，其个位数立方和等于个数本身
# for i in range(100,1001):
#     ge = i % 10
#     shi = i // 10 % 10
#     bai = i // 100
#     if ge ** 3 + shi ** 3 + bai ** 3 == i:
#         print(i)

#写一个程序，不断的输入内容，如果输入的内容是exit,打印程序结束后，结束该程序

while True:
    content = input('请输入内容')
    if content == 'exit':
        print('程序结束')
        break
