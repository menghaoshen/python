# 声明一个字典保存一个学生的信息，学生信息中包括: 姓名、年龄、成绩(单科)、电话、性别(男、女、不明)
# student = {'zhagnsan':'zhangsan','age':18,'score':98,'tel':'13888888888','gender':'female'}

# 声明一个列表，在列表中保存6个学生的信息
students = [{'name': 'zhangsan', 'age': 18, 'score': 98, 'tel': '13888888888', 'gender': 'female'},
            {'name': ';lsihi', 'age': 19, 'score': 95, 'tel': '13777777777', 'gender': 'male'},
            {'name': ';王五', 'age': 21, 'score': 97, 'tel': '13699999999', 'gender': 'unknown'},
            {'name': 'chris', 'age': 17, 'score': 58, 'tel': '13999999999', 'gender': 'male'},
            {'name': 'jack', 'age': 23, 'score': 52, 'tel': '1388899999', 'gender': 'femal'},
            {'name': 'tony', 'age': 15, 'score': 98, 'tel': '13888999888', 'gender': 'unknown'}
            ]
# (1) 统计不及格学生的个数
# (2) 打印不及格学生的名字和对应的成绩
# (3) 统计未成年学生的个数
# (4) 打印手机尾号是8的学生的名字
# (5) 打印最高分和对应的学生的名字
count = 0
teenager_count = 0
max_score = students[0]['score']  # 假设第0个学生的成绩是最高分
max_index = 0  # 假设最高分的学生下标是0
for i, student in enumerate(students):
    if student['score'] < 60:
        count += 1
        print('%s不及格，分数是%d' % (student['name'], student['score']))
    if student['age'] < 18:
        teenager_count += 1
    # if student['tel'].endswith('8'):  # 8结尾的
    if student['tel'][-1] == '8':  # 8结尾的
        print('%s的手机号以8结尾' % student['name'])
    if student['score'] > max_score:  # 遍历时，发现了一个学生的成绩大于假设的最大数
        max_score = students['score']
        max_index = i  # 修改最高的分的同时，把最高分的下标也修改了

print('不成年的学生有{}个'.format(teenager_count))
print('不及格的学生有%d' % count)
print('最高成绩是%d' % max_score)
print('最高分名字是%s' % students[max_index]['name'])  # 有可能会有并列第一的情况
for student in students:
    if student['score'] == max_score:
        print('最高分是%s' % student['name'])
# (6) 删除性别不明的所有学生(这个地方有个坑，跳不出来的话大家可以在群里套路，或者等老师的解答)
i = 0
# while i < len(students):
#     if students[i]['gender'] == 'unknown':
#         students.remove(students[i]) #每remvoe一个，下标要减一
#         i -= 1
#     i += 1
# print(students)
print('--------------------------------')
# (7) 将列表按学生成绩从大到小排序(选做)
for j in range(0, len(students) - 1):
    for i in range(0, len(students) - 1):
        if students[i]['score'] < students[i + 1]['score']:
            students[i], students[i + 1] = students[i + 1], students[i]
print(students)
