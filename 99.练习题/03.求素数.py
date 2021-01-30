#素数也叫质数，除了1和它本身以外，不能再被其他的任何数整除
for i in range(2,101):

    for j in range(2,i):
        if i % j == 0: #i 除以某一个数字，除尽了i就是合数
            break #结束内循环
    else:
        print(i,'是质数')