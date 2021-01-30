#外循环控制行数，内循环控制列数
j = 0
while j < 9:
    j += 1
    i = 0
    while i < j:
        i += 1
        print(i,'*',j,'=',(i * j),sep="",end=' ')
    print()