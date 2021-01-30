#函数就是一堆准备好的代码，在需要的使用调用这一堆代码
#正常的代码，可读性很差，维护性太差

#把多行代码打包成一个整体函数
#在python里面，使用关键字def 来声明一个函数

#def 函数名()
#   函数要执行的操作

#函数定义好以后，不会自动执行，需要调用
def tell_stroy():
    print('从前有个山')
    print('山上有个庙')
    print('庙里有个老和尚')
    print('还有一个小和尚')
    print('老和尚在给小和尚讲故事')
    print('故事的内容是')

age = int(input('请输入孩子的年龄'))
if 0 <= age < 3:
    for i in range(5):
        tell_stroy()
elif 5 > age >= 3:
    tell_stroy()