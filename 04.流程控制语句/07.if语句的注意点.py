#1.区间判断
# score = float(input('请输入你的成绩：'))
#
# #在python里面可以使练习的区间判断
# if 60 > score >= 0:
#     print('没有及格')

#2. 隐式类型转换
# if 4:  #if 后面的需要一个bool 类型的值，如果if后面不是布尔值，会自动转换成布尔类型
#     print('hello world')

#3. 三元表达式（对if ... else 的简写）

num1 = int(input('请输入一个数字'))
num2 = int(input('请在输入一个数字'))
#普通写法
# if num1 > num2:
#     x = num1
# else:
#     x = num2
#三元表达式
x = num1 if num1 > num2 else num2
print(x)