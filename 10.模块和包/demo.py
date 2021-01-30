# __all__ = ['m', 'test']  # 限制外面能调用的函数或者方法
m = 'yes'
n = 100


def test():
    print('我们demo里面的test方法')


def foo():
    print('我是demo模块里面的foo方法')


def dvi(a, b):
    return a / b


#__name__:直接运行的话是值是__main__
# 如果这个py文件作为一个模块导入的时候，值是文件名
if __name__ == '__main__':
    print('测试一下dvi函数，结果是devi', (4 / 2))
