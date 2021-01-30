from functools import reduce  # 导入模块的语法

# reduce 以前是个个内置的函数
# 内置函数和内置的类都在builtins.py 文件里面,求加法的运算
score = [100, 89, 76, 87]
print(reduce(lambda ele1, ele2: ele1 + ele2, score))



students = [
    {'name':'zhansan','age':18,'score':98,'height':180},
    {'name':'lisi','age':19,'score':95,'height':185},
    {'name':'wanwu','age':18,'score':85,'height':170},
    {'name':'jack','age':20,'score':80,'height':175}
]

def bar(x,y):
    #x = 0
    # y =  {'name':'zhansan','age':18,'score':98,'height':180},
    #x = 18
    # {'name':'lisi','age':19,'score':95,'height':185},

    return x+ y['age']


print(reduce(bar, students, 0))
print(reduce(lambda x,y:x+y['age'],students,0))