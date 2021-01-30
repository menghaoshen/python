# 1.2 g，记录下哪些数据被拷贝，哪些没有拷贝和拷贝路径。
# 2、读取 1 中的日志，并打印拷贝数据路径
import os
import shutil
import  sys
path = 'F:/培训数据/1.2数据/'
dst = 'F:/test'
for src, dirnames, filenames in os.walk(path):
    count = 0
    dst = os.path.basename(src)
    dest = 'F:/test/' + dst
    dirname = os.path.basename(src)
    for file in filenames:
        count += 1

    if count > 20:
        file1 = open('./copy.log', 'a', encoding='utf8')
        print('已经拷贝的文件夹:{}，拷贝的路径:{}'.format(dirname,src),file=file1)
        # shutil.copytree(src,dest) #被拷贝的日志
        # print('已拷贝数据的路径:{}'.format(src.split('路径:')[-1]), end='\n')
        file1.close()
    else:
        file2 = open('./not_copy.log','a',encoding='utf8')
        print('未经拷贝的文件夹:{}，未拷贝的路径:{}'.format(dirname,src),file=file2)
        file2.close()


file3 = open('./copy.log','r',encoding='utf8')
#打印已经拷贝的文件夹路径
for i in file3.readlines():
    print('已拷贝数据的路径:{}'.format(i.split('路径:')[-1]),end='')