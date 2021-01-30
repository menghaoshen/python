# = 符号在计算机里面是赋值运算符
#== 符号在比较运算符

import  random
# 随机数模块random
#radom.randint(a,b) ==> 能够生产[a,b]的随机整数
computer = random.randint(0,2)
print('电脑出的是',computer)

player = int(input('请输入 (0) 剪刀，（1）石头 （2）布：'))
print('用户输入的是：',player)



if (player == 0 and computer == 2 ) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print('恭喜您赢了')
elif player == computer:
    print('平局')
else:
    print('您输了')