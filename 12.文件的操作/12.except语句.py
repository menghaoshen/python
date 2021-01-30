#try ...expect 语句用来处理程序运行过程中的异常
try:
    person = {'name':'zhangsan'}
    print(person['age'])
    1 / 0
    file = open('ddd.txt')
    print(file.read())
    file.close()
# except Exception as e: #Exception 是所有异常的父类
#     print(e)
except (FileNotFoundError,ZeroDivisionError,KeyError) as e: #指定类型的异常
    print(e)

