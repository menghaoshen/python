import os
import sys


def get_num(path):
    num = 0
    folder_num = 0
    dirs = os.listdir(path)
    for dir_ in dirs:
        onepath = os.path.join(path, dir_)
        if os.path.isfile(onepath):
            continue
        folders = os.listdir(onepath)
        folder_num += len(folders)

        for folder in folders:
            deeppath = os.path.join(onepath, folder)
            files = os.listdir(deeppath)
            for file in files:
                if file.endswith('dcm') or file.endswith('DCM'):
                    num += 1
                    print(deeppath)
                    break 
    print("共{}个目录，其中{}个包含dcm".format(folder_num, num))


if __name__ == '__main__':
    if len(sys.argv) >1:
        path = sys.argv[1]
        get_num(path)
    else:
        print("命令行后面必须跟参数： python count.py /media/xbsj/dcm")