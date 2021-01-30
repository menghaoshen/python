# if 语句里面在嵌套if
ticket = input('是否买票了？Y/N')
if ticket == 'Y':
    print('买票了，可以进站')
    safe = input('安检是否通过?Y/N')
    if safe == 'Y':
        print('安检通过了，进候车室')
    else:
        print('进站了，但是安检没有通过')
else:
    print('没有买票，请去买票')