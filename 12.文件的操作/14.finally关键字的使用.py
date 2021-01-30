file = open('../98.培训题/98.培训题.zip','rb')
try:
    while True:
        content = file.read(1024)
        if not content:
            break
        print(content)
finally:  #最终都会被执行的代码
    print('文件被关闭了')
    file.close()