
import random
#nums = [1, 2[100, 200, 500], 3, 4, 5]
#一个学习，有3个办公司，现在有8个老师等待工位的分配，请编写程序，完成随机分配
teachers = ['A','B','C','D','E','F','G','H','I','J']
rooms = [[],[],[]]

for teacher in teachers:
    room = random.choice(rooms) #choice 从列表里随机选择一个数据
    room.append(teacher)

print(rooms)
#第0个房间有3个人，分别是....
for i,room in enumerate(rooms):  #enumerate 带下标的循环 i，就是下标
    print('房间%d里面一共有%d个老师，分别是' % (i,len(room)),end='\t')
    for teacher in room:
        print(teacher,end='\t')
    print()