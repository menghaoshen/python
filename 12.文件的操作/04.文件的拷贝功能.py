import os

file_name = input('请输入一个文件的路径：')  # 复制文件

if os.path.isfile(file_name):

    # 打开旧文件
    odl_file = open(file_name, encoding='gbk')
    # 方法一
    # name = file_name.rpartition('.') #切开字符，变成元组 rpartition默认从后面切
    # new_file = name[0] + '.back' + name[2]
    # 方法二
    names = os.path.splitext(file_name)  #splitext 默认从后面切
    print(names)
    new_file = names[0] + '.bak' + names[1]
    new_file = open(new_file, 'w', encoding='gbk')  # 打开一个新文件，用于写入

    # 把旧文件的数据读取出来，写到新文件
    new_file.write(odl_file.read())
    odl_file.close()
    new_file.close()
else:
    print('您输入的文件不存在')
