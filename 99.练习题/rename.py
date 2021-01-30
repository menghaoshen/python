import os
path=input('请输入文件路径(结尾加上/)')

#获取目录下面所有有的文件，存入列表中
filelist=os.listdir(path) 

n = 0

for i in filelist:
    #旧文件名
    oldname=path+filelist[n]
    #新文件名
    newname=path+'a'+str(n+1)+'.txt'
    #使用os模块中的rename 方法对文件改名
    os.rename(oldname,newname)
    print(oldname,'---->',newname)
    n+=1