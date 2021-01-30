#with 关键
# file = open('./err.log','r',encoding='utf8')
# file.read()
# file.close()
try:
    with open('./logs.txt','r',encoding='utf8') as file:
        file.read() # 不需要再手动关闭文件了，
        #file.close（） with 关键字会帮助我们关闭文件
except FileNotFoundError:
    print('文件没有找到')

#with 上下文管理器,很多需要手动需要关闭的连接
#比如文件连接，socket连接，数据库连接，都能使用wiht关键自动关闭
#with 关键字后面后面的对象，需要实习__enter__ 和__exit__魔法方法