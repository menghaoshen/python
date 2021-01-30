# 求斐波那契数列中的n个数的值，n是个整数

#求斐波那契树里第12个数
#前两个数是当前数的和
#1,1,2,3,5,8,13,21,34,55,89,144
n = int(input('请输入你要第几个斐波那契数：'))
#
#
num1 = 1
num2 = 1
#第3个数交换1次
#第四次交换2次1
#第五次交换3次
#第n个交换n-2
for i in range(0,n - 2):
    a = num1
    num1 = num2
    num2 = a + num2
print(num2)

# a = num1
# num1 = num2
# num2 = a + num2
# print(num2)
