#判断用户输入的是不是数字
num=input("输入一个数字：").strip()
#print(type(eval (num)))
#当num="123",输出int
#当num="1.234",输出float
if num.replace(".",'').isdigit():
    if num.count(".") ==0:
        print('int')
    elif num.count(".")==1:
        print('float')
else:
    print('既不是ini类型，也不是float类型')