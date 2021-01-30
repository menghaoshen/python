#python 里面用一个循环，打印三角形

# i = 0
# while i < 5:
#     i += 1
#     print('*' * i,end='\n')


#打印不换行
# print('*',end=' ')
# print('*',end=' ')
# print('*',end=' ')
# print('*',end=' ')
# print('*',end=' ')
#外循环控制行数，内循环控制列数
j = 0
while j < 10: #控制行数
    j += 1
    i = 0
    while i < 8: #控制每行的列数
        i += 1
        print('*',end=' ')
    print()