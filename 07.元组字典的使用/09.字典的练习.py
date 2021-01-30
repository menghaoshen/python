persons = [
    {'name': 'zhangsan', 'age': 18},
    {'name': 'lishi', 'age': 20},
    {'name': 'wangwu', 'age': 19},
    {'name': 'jerry', 'age': 21}
]

# 让用户输入姓名，如果姓名已经存在，提示用户，如果名字不存在，继续输入年龄，并存在列表里面
x = input('请输入您的姓名：')

for person in persons:
# if name in person #in 运算符，如果直接用在字典上，是用来判断key是否存在，而不value
    if person['name'] == x:
        print('您输入的名字存在')
        break
else:
        print('您输入的名字不存在')
        #创建一个新的字典
        new_person = {'name':x }
        y = int(input('请输入你的年龄'))
        new_person['age'] = y
        #把这个新的字典添加到persons列表里面
        persons.append(new_person)
        print('添加用户成功')
print(persons)