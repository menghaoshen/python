import csv

# file = open('./demon.csv','w',encoding='utf8',newline='') #打开一个文件 #newline='' 写入不换行
# w = csv.writer(file)
# w.writerow(['name','age','score','city'])
# # w.writerow(['张三','90','19','河南'])
# # w.writerow(['李四','99','20', '驻马店'])
# w.writerow(
#     [
#         'name','age','score','city',
#         '张三','90','19','河南',
#         '李四','99','20','驻马店'
#
#     ]
# )

#文件的读取
file = open('info.csv','r',encoding='gbk',newline='')
r = csv.reader(file)
for data in r:
    print(data)
file.close()