# 统计 1.2 文件夹中图片数量多余 20 的文件夹个数，并将其拷贝出来。
# 拷贝能跑通，但是统计功能没有体现出来。可以打印出有多少个文件是多余20张的，占总数比例是多少。
# 另外可以出查一下walk函数的具体用法。

import os
import shutil

def copy(path,dest):
    # path = 'F:/培训数据/1.2数据/'
    # dst = 'F:/test'
    dirsum = 0
    total = len(os.listdir(path))
    for src, dirnames, filenames in os.walk(path):
        count = 0
        dst = os.path.basename(src)
        dest = 'F:/test/' + dst

        for file in filenames:
            count += 1
        if count > 20:
            dirsum += 1
        print(src, '----->',dest)
    print('总共有{}个文件夹的文件是多余20张,占总数的比例是{:.2%}'.format(dirsum, (dirsum / total)))
    # shutil.copytree(src,dest)

if __name__ == '__main__':
    copy('F:/培训数据/1.2数据/','F:/test')