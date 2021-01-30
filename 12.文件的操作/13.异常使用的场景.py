# age = input('请输入您的年龄')
# if age.isdigit():
#     age = float(age)
#     if age > 18:
#         print('欢迎来到我的网站')
#     else:
#         print('未满18，请离开')
# else:
#     print('输入的不是数字')
age = input('请输入您的年龄')
try:
    age = float(age)
except ValueError as e:
    print('输入的不是数字')
else:
    if age > 18:
        print('欢迎来到我的网站')
    else:
        print('未满18，请离开')



