import os
import sys


def get_num(path):
    num = 0
    dirs = os.listdir(path)
    for dir_ in dirs:
        onepath = os.path.join(path, dir_)
        # print((onepath))
        if os.path.isfile(onepath):
            continue
        num += len(os.listdir(onepath))
    print("共拷贝了{}个文件夹".format(num))


if __name__ == '__main__':
    if len(sys.argv) >1:
        path = sys.argv[1]
        get_num(path)
    else:
        print("命令行后面必须跟参数： python count.py /media/xbsj/dcm")