def test(a, b):
    x = a // b
    y = a % b

    # 一般情况下面，一个函数最多只会执行一个retur语句
    # 特殊请求下，一个函数可能会执行多个return语句
    # return [x, y]
    return x, y  #默认是就是元组
    # return  x ,y   #不能写个两个return，程序看到return 就结束了，


result = test(13, 5)
print('商是{}，余数是{}'.format(result[0], result[1]))
shang,yushu = test(8,3) #元组的拆包
print('商是{}，余数是{}'.format(shang, yushu))
