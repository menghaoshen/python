import os

file_name = input('输入一个文件路径')

if os.path.isfile(file_name):
    odl_file = open(file_name, 'rb',) #读二进制
    name = file_name.rpartition('.')
    new_file_name = name[0] + '.back.' + name[2]
    new_file = open(new_file_name,'wb') #写二进制
    while True:
        content = odl_file.read(1024) #一次读1024 ，写完为止
        new_file.write(content)
        if not content:
            break
    odl_file.close()
    new_file.close()
else:
    print('')
