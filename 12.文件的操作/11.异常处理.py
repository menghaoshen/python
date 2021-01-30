# 在程序运行中，由于编码不规范等造成程序无法正常执行，此时程序就会报错
# 健壮性，很多开发语言都有异常处理机制
#
def dvi(a, b):
    return  a / b
try:
    x = dvi(5,1 ) #程序出错会立刻调到except 语句
    print('呵呵呵')
except Exception as e:
    print('程序出错了')
else: #如果程序没有出错，会执行else语言
    print('计算的结果是',x)