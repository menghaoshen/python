#函数的文档说明
def add (a:int,b:int): #期望的类型是int类型
    """
    这个函数将两个数字相加得到结果
    :param a:  第一个数字
    :param b:  第二个数字
    :return:  两个数字相加的结果
    """
    return  a + b
print(add(1,2))
print(add('hello', 'world'))

#查看函数的文档说明
help(add)
help(print)

#参数的类型我们没法限制，只能建议
#看到114集