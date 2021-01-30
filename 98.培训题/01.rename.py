# 作业：将 1.1 文件夹中的 59 个 json 分别改名为 01_原文件名.json 到 59_原文件名.json
import os

path = 'F:/培训数据/1.1数据/GYF-GS-0919-59cases/'
filelist = os.listdir(path)
n = 0
#修改文件名
for file in filelist:
    n += 1
    # number = str(n).zfill(2)
    olaname = path + file
    newname =path + str(n).zfill(2) + '_' + file #str 字符串拼接.zfill 填充字符串
    # print(newname)
    # os.rename(olaname,newname)
    print(olaname,'------>',newname)

# 再修改回来
# path = 'C:/Users/admin/Desktop/培训数据/1.1数据/GYF-GS-0919-59cases/'
# filelist = os.listdir(path)
# n = 0
# for file in filelist:
#     n += 1
#     old_name = path + file
#     num,new_file = file.split('_') #切割文件名
#     new_name = path + new_file
#     os.rename(old_name,new_name)
#     print(old_name, '------>', new_name)

