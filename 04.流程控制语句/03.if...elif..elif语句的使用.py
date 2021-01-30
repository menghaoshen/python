score = float(input('请输入您的成绩:'))

#多个if语句，语句和语句之间，不存在关联
# if 60 > score >= 0:
#     print('你个垃圾')
#
# if 80 > score >= 60:
#     print('一般般')
#
# if 90 > score >= 80:
#     print('还不错')
#
# if 100 >= score >= 90:
#     print('真厉害')

#有关联关系的
if 60 > score >=0:
    print('你个垃圾')
elif 80 > score >= 60:
    print('一般般')
elif 90 > score >= 80:
    print('还不错')
elif 100 >= score >= 90:
    print('真厉害')
else:
    print('请输入正确的分数')